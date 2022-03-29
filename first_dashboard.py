import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

image = Image.open('lg.png')

st.image(image, width = 200)
#TITLE
st.title('Dashboard Kelompok 5')
st.markdown('List Kelompok:')
st.markdown('1. Ni Putu Ayu Triana (Aachen)')
st.markdown('2. Desak Putu Sri Wulandari (Aachen)')
st.markdown('3. Ni Komang Santi Cahyani (Aachen)')
st.markdown('4. Ni Wayan Windayani (Aachen)')
st.markdown('5. Winda Kuncorowati (Apollo)')
st.markdown('6. I Gede Krisna Pratama Jumenatha (Apollo)')
#HEADER
st.header("Ini adalah Data Covid-19 di Indonesia")

#WRITE
st.write("Dataframe Data yang Telah dibersihkan")
data = pd.read_csv('Covid_19_Indonesiaclean.csv')

# BUTTON
if st.button("Lihat Dataframe"):
    st.write(data)

# CHECKBOX
info = data.nunique()
if st.checkbox("Lihat Jumlah Elemen Unik"):
    st.write(info)

# SELECT
Location = st.selectbox("Select Dataframe of Location", data.Location.unique())

# RADIO BUTTON
Island = st.radio("Select Dataframe of Island", data.Island.unique())

st.write(data[
    (data.Location == Location) & (data.Island == Island)])   

# Melihat jumlah kasus
st.write("Lihat Jumlah Kasus")
positif     = st.checkbox("Kasus Positif")
meninggal   = st.checkbox("Kasus Meninggal")
sembuh      = st.checkbox("Kasus Sembuh")  
if (meninggal and sembuh and positif):
    data4 = data[['Date', 'Total_Cases', 'Total_Deaths', 'Total_Recovered']]
    st.write(data4)
elif (positif == True) and (meninggal == True):
    data1 = data[['Date', 'Total_Cases', 'Total_Deaths']]
    st.write(data1)
elif (positif and sembuh):
    data2 = data[['Date', 'Total_Cases', 'Total_Recovered']]
    st.write(data2)
elif (meninggal and sembuh):
    data3 = data[['Date','Total_Deaths', 'Total_Recovered']]
    st.write(data3)
elif meninggal:
    data5 = data[['Date','Total_Deaths']]
    st.write(data5)
elif sembuh:
    data5 = data[['Date','Total_Recovered']]
    st.write(data5)
elif positif:
    data5 = data[['Date', 'Total_Cases']]
    st.write(data5)
else:
    data4 = data[['Date','Total_Cases', 'Total_Deaths', 'Total_Recovered']]
    st.write(data4)

# Membuat PLOT Normalisasi Data
st.markdown('Plot Normalisasi')
arr = np.random.normal(1, 1, 100)
st.write(arr)
fig, ax = plt.subplots()
plt.hist(arr, bins=20)
st.pyplot(fig)

#Membuat plot kasus perhari
st.markdown('Plot Kasus Perhari')
df_can_col = st.selectbox("Pilih Kasus", ['Total_Cases', 'Total_Deaths', 'Total_Recovered'])
fig = px.line(data, x='Date', y=df_can_col)
st.plotly_chart(fig)
