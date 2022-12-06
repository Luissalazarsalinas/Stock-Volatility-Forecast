import sqlite3

from fastapi import FastAPI, status
import uvicorn
from app.schemas import  PredictIn, PredictOut
from app.config import settings
from app.data import AlphaVantageApi, SQLRepository
from app.model import GrachModel

# Funtion to build the model
def build_model(ticker, use_new_data):

    # Create DB connection
    connection = sqlite3.connect(settings.database_name, check_same_thread=False)

    #create a SQLrepository
    repo = SQLRepository(connection=connection)

    # Create the model
    model = GrachModel(
        ticker= ticker,
        repo= repo,
        use_new_data= use_new_data
    )
    return model

# Create API object
app = FastAPI()


# Predict path
@app.post("/predict", status_code= status.HTTP_201_CREATED, response_model=PredictOut)
def fit_model(request:PredictIn):

    # Createa dict
    response = request.dict()

    try:

        # Create the model
        model = build_model(ticker=request.ticker, use_new_data=request.use_new_data)

        # Wrangle data
        model.wrangle_data(n_observations=request.n_observations)

        # Train the model
        model.fit_model(p=request.p, q=request.q)

        # Create a prediction
        prediction = model.predict_volatility(horizon=request.n_days)

        # add response
        response["success"] = True

        # add  Forescast
        response["forecast"] = prediction

        # add Metricts
        response["metrics"] = {"AIC" : model.aic, "BIC": model.bic} #f"AIC : {model.aic} BIC : {model.bic}"

        # Add message
        response["message"] = f"{request.ticker} Volatility Forecast"

    except Exception as e:
        # add to response
        response["success"] = False
        # Add forecast
        response["forecast"] = {}
        # add Metricts
        response["metrics"] = " "
        # add to Forescast
        response["message"] = str(e)
    
    return response