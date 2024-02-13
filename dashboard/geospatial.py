
import numpy as np
import pandas as pd
import folium
import re
import geopandas
import matplotlib
import matplotlib.pyplot as plt





class GeoSpatial:
    def __init__(self):
        pass



    def make_chloropleth(self, df,area):
        sg_geojson=geopandas.read_file('./data/regions.geojson')
        sg=(sg_geojson.loc[sg_geojson['name'].isin(area)])
        sg.reset_index(drop=True, inplace=True)

        towns = dict(df['town'].value_counts())
        sg["sales"] = sg["name"].map(towns)
        return sg.explore("sales", cmap="copper",tiles="CartoDB positron")  
    


    def make_chloropleth_price(self, df,area,room_type):
        sg_geojson=geopandas.read_file('./data/regions.geojson')
        sg=(sg_geojson.loc[sg_geojson['name'].isin(area)])
        sg.reset_index(drop=True, inplace=True)

        flat = df[df["flat_type"] == room_type]
        price=dict(flat.groupby(flat['town'])["price"].mean().round(0))

        
        sg["ave_price"] = sg["name"].map(price)
        return sg.explore("ave_price", cmap="viridis",tiles="CartoDB positron")