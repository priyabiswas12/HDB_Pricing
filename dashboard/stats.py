import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import warnings





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
    


 
    

    def get_piechart_ft(self,df,others_ls,region):
        if region == "ENTIRE SINGAPORE":
            r_df=df
        else:
            r_df=df[df['town']== region]

        flat_types = dict(r_df['flat_type'].value_counts())

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
    
    

    def pricevlease(self, df):
        g = sns.FacetGrid(df, col="town", col_wrap=5)
        g.map(sns.scatterplot, "remaining_lease","price",alpha=0.5)
        g.add_legend()
        return g
    


    def pricevdist(self, df):
        g = sns.FacetGrid(df, col="town", col_wrap=3)
        g.map(sns.scatterplot, "mrt_dist","price",alpha=0.5)
        g.add_legend()
        return g
    

    def pricevloc_box(self, df,room_type):
        warnings.filterwarnings('ignore')
        flat = df[df["flat_type"] == room_type]
        g= sns.catplot(data=flat,x='town',y='price',kind='box',aspect=1.5)
        
        g.set_xticklabels(rotation=90)
        g.figure.suptitle("Price Distribution of Chosen Flat Type",fontsize=15)
        return g




        
