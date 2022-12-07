# import os 
# import glob
# import joblib

import pandas as pd
from arch import arch_model
from app.data import AlphaVantageApi

class GrachModel:

    def __init__(self, ticker):

        self.ticker = ticker
    # Methods
    def wrangle_data(self):
        
        # Intance 
        av = AlphaVantageApi()
        # get daily data
        df = av.get_daily(ticker=self.ticker)
        # Sort index
        df.sort_index(ascending = True, inplace = True)
        # Calculing the returns
        df["return"] = df["close"].pct_change()*100
        # stored a object data
        self.data = df["return"].dropna()
    
    def fit_model(self, p, q):
        
        # Train the model
        self.model = arch_model(
            self.data,
            p= p,
            q= q,
            rescale= False
        ).fit(disp=0)

        # Add metrics
        self.aic = self.model.aic
        self.bic = self.model.bic

        return self.model

    def __clean_prediction(self, prediction):
        
        # Start date
        start = prediction.index[0] + pd.DateOffset(days=1)
        # date range
        date_range = pd.bdate_range(start= start, periods= prediction.shape[1])
        # Create prediction index labels, ISO 8601 format
        prediction_index = [d.isoformat() for d in date_range]
        # Extract predictions from DataFrame, get square root
        data = prediction.values.flatten()**0.5
        # Join data using a serie
        predict_formatted = pd.Series(data, index=prediction_index)

        # Return the data into a dict 
        return predict_formatted.to_dict()

    def predict_volatility(self, horizon:int = 5):
        
        # Forecast
        prediction = self.model.forecast(
            horizon= horizon,
            reindex= False
        ).variance

        forecast = self.__clean_prediction(prediction)

        return forecast




    


