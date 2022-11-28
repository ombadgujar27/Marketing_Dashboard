import streamlit as st #Webdevelopment
import pandas as pd #read_datasets , manipulation
import numpy as np #np mean , np var
import json
import requests 
import plotly.express as px #iteractive charts


#read dataset  (CSV File)
data = pd.read_json("C:\\Users\\OM\\Desktop\\om\\data.json")

 
#title of dashboard
st.title("MARKETING DASHBOARD")

l0 = data.columns
l1 = []
l2 = []

i=0
for i,x in enumerate (l0) :
    if 'orderbook' in x :  #Creating a table 
        l1.append(x)
    elif 'trade' in x:     #Making chart
        l2.append(x)
    i += 1

data1 = pd.DataFrame(l1)
data2 = pd.DataFrame(l2)

st.markdown("Dataset", unsafe_allow_html=True)
Dataset = st.checkbox('')  # check box

if Dataset:     
    st.write(data)

def interactive_plot1(l0):
    st.markdown("<h2 style='text-align: center; color: White; font-size:25px; '>Line Chart</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    x_axis_val = col1.selectbox('Select the X-axis', options=data1)
    y_axis_val = col2.selectbox('Select the Y-axis', options=data2)

    plot = px.line(data, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot)


def interactive_plot2(l0):
    st.markdown("<h2 style='text-align: center; color: White; font-size:25px; '>Bar Chart</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    x_axis_val = col1.selectbox('Select the X-axis', options=data1)
    y_axis_val = col2.selectbox('Select the Y-axis', options=data2)

    plot = px.bar(data, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot)


def interactive_plot3(l0):
    st.markdown("<h2 style='text-align: center; color: White; font-size:25px; '>Area Chart</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    x_axis_val = col1.selectbox('Select the X-axis', options=data1)
    y_axis_val = col2.selectbox('Select the Y-axis', options=data2)

    plot = px.area(data, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot)


def interactive_plot4(l0):
    st.markdown("<h2 style='text-align: center; color: White; font-size:25px; '>Scatter Chart</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    x_axis_val = col1.selectbox('Select the X-axis', options=data1)
    y_axis_val = col2.selectbox('Select the Y-axis', options=data2)

    plot = px.scatter(data, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot)



st.sidebar.title('Navigation')

option=st.sidebar.radio('Select what you want to display:',['Line Chart','Bar Chart','Area Chart','Scatter Chart'])

if option == 'Line Chart':
  interactive_plot1(data)
elif option == 'Bar Chart':
  interactive_plot2(data)
elif option == 'Area Chart':
  interactive_plot3(data)
elif option == 'Scatter Chart':
  interactive_plot4(data)