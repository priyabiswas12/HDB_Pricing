import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns





class Stats:
    def __init__(self):
        pass
    

    def pricevsmonth(self, df,ft):
        fig, ax = plt.subplots()
        
        for ftype in ft:
            flat = df[df["flat_type"] == ftype]
            flat.groupby(flat["month"])["price"].mean().plot()

        ax.legend(ft)
        plt.ylabel("Price")
        plt.title("Average Price Over the Months")
        return fig
    


    def pvm_region(self, df,ft,region):
        r_df=df[df['town']== region]
        present=[]
        fig, ax = plt.subplots()
        for ftype in ft:
            flat = r_df[r_df["flat_type"] == ftype]
            if flat.empty:
                pass
            else:
                present.append(ftype)
                flat.groupby(flat["month"])["price"].mean().plot()

        ax.legend(present)
        plt.ylabel("Price")
        plt.title("Average Price of selected town")
        return fig
    


 
    

    def get_piechart_ft(self,df,others_ls):
        flat_types = dict(df['flat_type'].value_counts())

        def get_others(dic, key):
            x=dic.get(key)
            if x== None:
                return 0
            else:
                return x
            
        combined=0
        for ot in others_ls:
            combined += get_others(flat_types, ot)
            flat_types.pop(ot, None)
        flat_types["OTHERS"]= combined
    

        labels = tuple(flat_types)
        sizes = list(flat_types.values())

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        return (fig1)

        
