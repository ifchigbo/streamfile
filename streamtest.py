from turtle import width
import pandas as pd
from sqlalchemy import column
import streamlit as st
from PIL import Image
from streamlit.errors import Error
from covid import getDataSource,getCountryStats
import streamlit.components as comp 

st.set_page_config(
     page_title="Covid-19",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
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
        mycountry = getCountryStats(country)
        st.write(mycountry)

    #my
def allMethods():
    title_Section()
    displayInitialAnalysis()
    covidStatsCountry()

if __name__ == '__main__':
    allMethods()
