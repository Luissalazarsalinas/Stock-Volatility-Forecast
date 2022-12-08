
import pandas as pd
from app.data import AlphaVantageApi
from app.model import GrachModel

# Funtion to build the model
def build_model(ticker):
    # Create the model
    model = GrachModel(
        ticker= ticker,   
    )
    return model

def forecast_volatility(ticker:str, p:int = 1, q:int = 1, n_days:int = 5):

    response = {}
    
    try:
        # Create the model
        model = build_model(ticker=ticker)

        # # Wrangle data
        model.wrangle_data()

        # Train the model
        model.fit_model(p=p, q=q)

        # Create a prediction
        prediction = model.predict_volatility(horizon=n_days)

        # add response
        response["success"] = True

        # add  Forescast
        response["forecast"] = prediction

        # add Metricts
        response["metrics"] = {"AIC" : model.aic, "BIC": model.bic} #f"AIC : {model.aic} BIC : {model.bic}"

        # Add message
        response["message"] = f"{ticker} Volatility Forecast"

    except Exception as e:
        # add to response
        response["success"] = False
        # Add forecast
        response["forecast"] = {}
        # add Metricts
        response["metrics"] = {}
        # add to Forescast
        response["message"] = str(e)
    
    return response
