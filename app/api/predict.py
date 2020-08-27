import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator
from joblib import load
import os
from .dictionary import BoroughDict, NeighbourhoodDict, RoomTypeDict

log = logging.getLogger(__name__)
router = APIRouter()

filepath = os.path.join(os.path.dirname(__file__), "..",
                                     "assets",
                                     "rf_reg.joblib")


class AirBnB(BaseModel):
    """Use this data model to parse the request body JSON."""
    Borough: str = Field(..., example='Brooklyn')
    Neighbourhood: str = Field(..., example='Kensington')
    Room_type: str = Field(..., example='Private room')
    Minimum_nights: int = Field(..., example=1)
    Availability_365: int = Field(..., example=365)

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])
    
    def map(self):
        self.Borough = BoroughDict[self.Borough]
        self.Neighbourhood = NeighbourhoodDict[self.Neighbourhood]
        self.Room_type = RoomTypeDict[self.Room_type]


@router.post('/predict')
async def predict(AirBnB: AirBnB):
    """Predict AirBnB prices in NYC."""
    AirBnB.map()
    df = AirBnB.to_df()
    pipeline = load(filepath)
    y_pred = pipeline.predict(df)
    price = '$' + str(y_pred[0])
    return {'predicted_price ': price}
