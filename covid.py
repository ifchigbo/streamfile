import  pandas as pd
import seaborn as sb 
from matplotlib import pyplot as plt
import numpy as np
import geopandas as gpd
from pandas.errors import ParserError, MergeError, EmptyDataError

def getDataSource():
    data = pd.read_csv("covid_202207191347.csv")
    return data 

def getCountryStats(country):
    df = getDataSource()
    mycountry = df.loc[df['country'] ==  country]
    return mycountry

def getGroupedData():
    data = getDataSource()
    mygrouped_data = data.groupby(by='region').sum()['Deaths - newly reported in last 7 days', 'Transmission Classification']
    return(mygrouped_data.reset_index())