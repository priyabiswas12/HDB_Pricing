import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from datetime import datetime
import calendar
from dashboard.geospatial import GeoSpatial
from dashboard.stats import Stats
from dashboard.df_preprocessing import Preprocess
from streamlit_folium import st_folium
import matplotlib
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')



#######################
# Page configuration
st.set_page_config(
    page_title="HDB Resale Dashboard",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")



df = pd.read_csv('data/resale_total.csv',low_memory=False)
p=Preprocess()
df=p.process_resale(df)




with st.sidebar:
    st.title('HDB Resale Dashboard')
    
    month_list = list(df.month.unique())
    start, end =st.select_slider("Select a range of months", options=month_list, value=(month_list[0],month_list[-1]))
    start_format=calendar.month_abbr[start.month] + "-" + str(start.year)
    end_format=calendar.month_abbr[end.month] + "-" + str(end.year)
    st.write("You chose between:" , start, " to ", end )
    new_df=df[df['month'].between(start,end)]
   
   





   


#######################
# Dashboard Main Panel
col = st.columns((4.5, 3, 2), gap='small')


#MAPS
resale_areas=['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
       'BUKIT TIMAH', 'CHOA CHU KANG', 'CLEMENTI',
       'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
       'KALLANG/WHAMPOA', 'MARINE PARADE', 'QUEENSTOWN', 'SENGKANG',
       'SERANGOON', 'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN',
       'LIM CHU KANG', 'SEMBAWANG', 'BUKIT PANJANG', 'PASIR RIS',
       'PUNGGOL',"CENTRAL AREA"]



with col[0]:
    st.markdown('#### Number of Total Sales Between {} to {}'.format(start_format, end_format))
    g= GeoSpatial()
    choropleth = g.make_chloropleth(new_df,resale_areas)
    st_folium(choropleth,width=700, height=400)

    st.markdown('#### Price/sqm of Chosen Flat Type')
    #st.markdown('#### Flat Type overview')
    #st.markdown('#### Average Rental Price of Chosen Flat Type')
    flat_type_ls= [ '3 ROOM', '4 ROOM', '5 ROOM', '2 ROOM','1 ROOM' ,'EXECUTIVE', 'MULTI-GENERATION']
    selected_ft= st.selectbox('Select a Flat Type', flat_type_ls)
    choropleth_price=g.make_chloropleth_price(new_df,resale_areas,selected_ft)
    st_folium(choropleth_price,width=700, height=400)

    s= Stats()
    #st.markdown('#### Price Distribution of Chosen Flat Type')
    splot6 = s.pricevloc_box(new_df,selected_ft)
    st.pyplot(splot6)



#STATS
    
resale_ft= ['1 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', '2 ROOM', 'EXECUTIVE','MULTI-GENERATION']

with col[1]:
    st.markdown('#### Pricing Overview')
    
    splot2 = s.pricevsmonth(new_df,resale_ft)
    st.pyplot(splot2)



    st.markdown('#### Town-specific Resale Price Trend')
    region = list(new_df.town.unique())
    selected_region= st.selectbox('Select a Town', region)
    splot4 = s.pvm_region(new_df,resale_ft,selected_region)
    st.pyplot(splot4)



    st.markdown('#### Distribution of Price vs Remaining Lease')
    splot6 = s.pricevlease(new_df)
    st.pyplot(splot6)



    
  


    


    
    






with col[2]:


    st.markdown('#### Top Model Types')
    df2 = new_df["flat_model"].value_counts().rename_axis('flat_model').to_frame('counts')

    st.dataframe(df2,
                column_order=("flat_model", "counts"),
                hide_index=True,
                width=None,
                column_config={
                    "flat_model": st.column_config.TextColumn(
                        "Flat Model",
                    ),
                    "counts": st.column_config.ProgressColumn(
                        "Number of Units Sold",
                        format="%f",
                        min_value=0,
                        max_value=max(df2.counts),
                    )}
                )



    st.markdown('#### Percentage of Flat Types Sold')
    others=["2 ROOM", "1 ROOM", "MULTI-GENERATION"]
    region2 = list(new_df.town.unique())
    region2.insert(0,  "ENTIRE SINGAPORE")
    selected_region2= st.selectbox('Select a Town', region2)
    splot5 = s.get_piechart_ft(new_df,others, selected_region2)
    st.pyplot(splot5)
  

    

    

    




    
