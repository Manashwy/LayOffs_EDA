from pandas.core.frame import DataFrame
import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('layoffs_data.csv')

side = ["About", "Data", "Analysis"]

st.sidebar.header('Sections')
st.sidebar.subheader('This webpage contains three sections as follows')
bar = st.sidebar.selectbox("Select one to see details:",side)

if bar == "About":
    st.header("About")
    st.subheader("this data...")
    st.write('''**Analysing the layoff dataset from kaggle**
*https://www.kaggle.com/datasets/theakhilb/layoffs-data-2022*

    This dataset was scraped from Layoffs.fyi with the hope to enable 
    Kaggle community to look into analyzing recent mass layoffs 
    and discover useful insights and patterns.

    Original dataset can be tracked at https://layoffs.fyi/

    Credits: Roger Lee

''')


elif bar == 'Data':
    "**The dataset:**"
    with st.expander("Show data", expanded=False):
        st.dataframe(df.head(5))

    col1,col2,col3 = st.columns(3) 
    with col1:

        rad = ["Top 50 companies with highest layoffs", "companies with full lay-offs"]
        if st.radio("Select:",rad) == rad[0]:
            st.dataframe(df.groupby('Company')['Laid_Off_Count'].sum().sort_values(ascending=False)[:50])
        else:# st.radio("Select:",rad) == rad[1]:
            st.dataframe(df.dropna().groupby('Company')['Percentage'].mean().sort_values(ascending=False)[:50])
    
    


elif bar == 'Analysis':
    st.header("Visual Analysis")
    st.subheader("Finding out important information using useful charts")
    kol1, kol2 = st.columns([1,2])
    with kol1:

        labs = ["Company","Location","Country","Stage","Industry"]

        lay = st.selectbox("LayOffs by: ",labs)
        
    st.area_chart(df.dropna().groupby('Company')['Laid_Off_Count'].sum(),width=30)



else:
    st.header('Thats it')
    st.subheader('Bye!')



