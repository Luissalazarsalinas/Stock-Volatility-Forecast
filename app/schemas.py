from pydantic import BaseModel
from typing import Optional

# Predict in
class PredictIn(BaseModel):
    ticker:str
    p:int
    q:int
    n_days: int
# predict in 
class PredictOut(PredictIn):
    success:bool
    forecast: dict
    metrics: dict
    message:str