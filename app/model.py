# import os 
# import glob
# import joblib

import pandas as pd
from arch import arch_model
from app.config import settings
from app.data import AlphaVantageApi, SQLRepository

class GrachModel:

    def __init__(self, ticker, repo, use_new_data):

        self.ticker = ticker
        self.repo = repo
        self.use_new_data = use_new_data

    # Methods
    def wrangle_data(self, n_observations):

        if self.use_new_data:
            # Intance 
            av = AlphaVantageApi()
            # get daily data
            new_data = av.get_daily(ticker=self.ticker)
            # Create a new table
            self.repo.insert_table(
                table_name = self.ticker,
                record = new_data,
                if_exists = "replace"
            )

        # Read data from the database
        df = self.repo.read_table(
            table_name = self.ticker,
            limit = n_observations+1
        ) 

        # Sort index
        df.sort_index(ascending = True, inplace = True)
        # Computing the returns
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




    


