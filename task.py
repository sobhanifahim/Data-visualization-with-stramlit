import streamlit as st
import numpy as np
import pandas as pd

df=pd.read_csv('preprocessed_dataset.csv',usecols=['Lat', 'Long'])
df.rename(columns = {'Lat':'LAT'}, inplace = True)
df.rename(columns = {'Long':'LON'}, inplace = True)
st.write(df.head())
st.map(df)