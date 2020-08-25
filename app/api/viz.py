from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px

router = APIRouter()

df = pd.read_csv("assets/clean_rent.csv")

@router.get('/map')
async def visual():
    """
    this takes the cleaned NYC rental dataset in csv format and makes interactive heatmap 

    ### Response
    JSON string to render with react-plotly.js
    """
    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", color="price",
                            hover_data=["neighbourhood_group",	"neighbourhood", "id"],
                            color_discrete_sequence=["fuchsia"], 
                            zoom=10, height=125)

    # Location Graph
    fig.update_layout(mapbox_style="open-street-map")

    # Layout Features
    fig.update_layout(width=1000, 
                    height=1000, 
                    margin={"r":1,"t":1,"l":1,"b":1})

    return fig.to_json()
