from pydantic import BaseModel
from typing import Optional

# Predict in
class PredictIn(BaseModel):
    ticker:str
    use_new_data:Optional[bool] = False
    n_observations: Optional[int] = None
    p:int
    q:int
    n_days: int
# predict in 
class PredictOut(PredictIn):
    success:bool
    forecast: dict
    metrics: dict
    message:str