import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator
from joblib import load
import os
#from .dictionary import BoroughDict, NeighbourhoodDict, RoomTypeDict

log = logging.getLogger(__name__)
router = APIRouter()

filepath = os.path.join(os.path.dirname(__file__), "..",
                                     "assets",
                                     "rf_reg_factorize.joblib")


class AirBnB(BaseModel):
    """Use this data model to parse the request body JSON."""
    Borough: int = Field(..., example=2)
    Neighbourhood: int = Field(..., example=109)
    Room_type: int = Field(..., example=2)
    Minimum_nights: int = Field(..., example=1)
    Availability_365: int = Field(..., example=365)

    #def to_df(self):
    #    """Convert pydantic object to pandas dataframe with 1 row."""
    #    return pd.DataFrame([dict(self)])


@router.post('/predict')
async def predict(AirBnB: AirBnB):
    """Predict AirBnB prices in NYC."""
    #AirBnB.map()
    #df = AirBnB.to_df()
    data = [2, 109, 2, 1, 365]
    columns = ['Borough', 'Neighbourhood', 'Room_type', 'Minimum_nights', 'Availability_365']
    df = pd.DataFrame(data, columns = columns)
    pipeline = load(filepath)
    y_pred = pipeline.predict(df)
    return {'predicted_price $': y_pred}
