import pandas as pd
import numpy as np
from datetime import datetime




class Preprocess:
    def __init__(self):
        pass


    def process_resale(self, df):

        df["month"] = pd.to_datetime(df["month"])
        df['month'] = df['month'].dt.to_period('M')
        df['price_per_sqm'] = df['resale_price'] / df['floor_area_sqm']
        df["flat_type"]=df["flat_type"].replace({'MULTI GENERATION': 'MULTI-GENERATION'})
        df['age'] = datetime.now().year -  df['lease_commence_date']
        df.rename(columns={'resale_price': 'price'}, inplace=True)

        return df
    

    def process_rental(self, df):

        df["rent_approval_date"] = pd.to_datetime(df["rent_approval_date"])
        df['rent_approval_date'] = df['rent_approval_date'].dt.to_period('M')
        df["town"]=df["town"].replace({'CENTRAL': 'CENTRAL AREA'})
        df.rename(columns={'rent_approval_date': 'month', 'monthly_rent': 'price'}, inplace=True)
        return df
    


