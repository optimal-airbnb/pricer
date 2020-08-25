import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator
from joblib import load

log = logging.getLogger(__name__)
router = APIRouter()


class AirBnB(BaseModel):
    """Use this data model to parse the request body JSON."""
    room_type: str
    availability_365: int
    neighbourhood: str

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

@router.post('/predict')
async def predict(AirBnB: AirBnB):
    """Predict AirBnB prices in NYC."""
    X_new = AirBnB.to_df()
    pipeline = load("assets/rf_reg.joblib")
    y_pred = pipeline.predict(X_new)[0]
    return {'predicted_price $': y_pred}
