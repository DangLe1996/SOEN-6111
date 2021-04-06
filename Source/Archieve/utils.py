
import dask.dataframe as df

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
from datetime import datetime

from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler


def transformDataIntoDateTime(data):
    data = data.set_index('State').drop(['countyFIPS', 'stateFIPS', 'County Name'], axis=1).compute()
    data = data.transpose()
    data = data.reset_index()
    data['dateTime'] = pd.to_datetime(data['index'])
    data = data.drop('index', axis = 1).set_index('dateTime')
    return data

class readDataClass:
    dataDF = ''
    filterByCounty = (lambda a: a['countyFIPS'] != 0)
    filterByState = (lambda a: a['countyFIPS'] == 0)

    def __init__(self, filePath):
        self.dataDF = df.read_csv(filePath)

    def getDataDF(self):
        return self.dataDF

    def getDataByFIPS(self, fips):
        return self.dataDFdataDF[self.dataDF.countyFIPS == fips]

    def getDataByDate(self, date):
        """
        Get a column of data using date
        :param dataDF:
        :param date:
        :return:
        """
        return self.dataDF[date]

    def getDateInterval(self,filterBy, startDate, endDate, interval):
        startIndex = self.getColumnIndex(startDate)
        endIndex = self.getColumnIndex(endDate)
        cols = list(range(startIndex,endIndex+1))
        cols = [1,2]+cols[::interval]
        countyData = self.dataDF[self.dataDF.apply(filterBy,axis = 1)]
        return countyData.iloc[:,tuple([cols])]

    def getCountyDateInterval(self, startDate, endDate, interval):
        startIndex = self.getColumnIndex(startDate)
        endIndex = self.getColumnIndex(endDate)
        cols = list(range(startIndex,endIndex+1))
        cols = [1,2]+cols[::interval]
        countyData = self.dataDF[self.dataDF.apply(self.getByCounty)]
        return countyData.iloc[:,tuple([cols])]

    def getStateDateInterval(self, startDate, endDate, interval):
        startIndex = self.getColumnIndex(startDate)
        endIndex = self.getColumnIndex(endDate)
        cols = list(range(startIndex,endIndex+1))
        cols = [1,2]+cols[::interval]
        countyData = self.dataDF[self.dataDF['countyFIPS'] == 0]
        return countyData.iloc[:,tuple([cols])]


    def getColumnIndex(self,columnName):
        return self.dataDF.columns.get_loc(columnName)