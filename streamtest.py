from turtle import width
import pandas as pd
from sqlalchemy import column
import streamlit as st
from PIL import Image
from streamlit.errors import Error
from covid import getDataSource,getCountryStats, getGroupedData
import streamlit.components as comp 
import seaborn as sb
from matplotlib import pyplot as plt

st.set_page_config(
     page_title="Covid-19 Data Processing",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     #menu_items={
     #   '''''
     #    'Get Help': '',
     #    'Report a bug':,
     #    'About': 
     #    '''
     #}
)
def title_Section():
    try:
        title = st.title("Data Display for Covid-19  Pandemic")
        return title
    except Error as error:
        print(error)

def displayInitialAnalysis():

    df = getDataSource()
    # create a dro down item list  to check for  the following;
    #NA
    #Columns
    #Get the First 10 data rows
    #Datatype of the columns of the data frame: 
    NaN = st.checkbox('Get the List of NaN in the Data Set')
    if NaN:
        try:
            st.write(df.isna().sum())
            st.write(df.isna())
        except Error as error:
            print(error)
    Columns = st.checkbox('Get Columns and Data Types')
    if Columns: 
        try:
            st.write(df.columns)
        except Error as error:
            print(error)

    Sample_Data = st.checkbox("Sub Data Sets")
    if  Sample_Data:
        try:
            st.write(df.head(10))
        except Error as error:
            print(error)

    Datatype = st.checkbox('Get  Column Data types')
    columns = []
    datatype =[]

    for items in  df.columns:
        columns.append(str(items))
    
    for items in df.dtypes:
        datatype.append(str(items))

    if  Datatype:
    
        try:        
            print(st.write(columns))
            print(st.write(datatype))
        except Error as error:
            print(error)
       
def covidStatsCountry():
    country = st.text_input("Get Statistics per Region")

    if  country:
        try:
            mycountry = getCountryStats(country)
            st.write(mycountry)
        except Error  as error:
            print(error)

# Get Regional Deathrates for the past 7 days
def groupedDatabyRegion():
    try:
        region = getGroupedData()
        return region 
    except Error as  error:
        print(error)

#Get plot from the regional data generated from motarlity  rates for the past 7 days
def getRegionalPlotData():
    plotvar =groupedDatabyRegion()
    plot = st.selectbox(
        "Select a Plot Style to Display",
        ['Bar Plot', 'Line Plot']
    )
    if plot == 'Bar Plot':
        try:
            fig = plt.figure(figsize=(25,15))
            sb.barplot(data=plotvar,y='Deaths - newly reported in last 7 days', x='region')
            st.pyplot(fig)
        except Error as error:
            print(error)
    elif plot == 'Line Plot':
        try:
            fig = plt.figure(figsize=(25,15))
            #sb.relplot(x='region', y='Deaths - newly reported in last 7 days',kind='line', data=plotvar)
            sb.lineplot(x='region', y='Deaths - newly reported in last 7 days', data=plotvar)
            st.pyplot(fig)
        except Error as error:
            print(error)
            

    


    #The main method that runs all files
def allMethods():
    sb.set_theme()
    title_Section()
    displayInitialAnalysis()
    covidStatsCountry()
    print(st.subheader('Regional Death Rate in  7 Days'))
    st.write(
        groupedDatabyRegion()   
    )
    getRegionalPlotData()

if __name__ == '__main__':
    allMethods()
