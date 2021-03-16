
from dask import dataframe as df

class readData:
    dataDF = ''

    def __init__(self, filePath):
        self.dataDF = df.read_csv(filePath).set_index('countyFIPS')

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

    def getDataByTimeInterVal(self, startDate, endDate, interval):
        startIndex = self.getColumnIndex(startDate)
        endIndex = self.getColumnIndex(endDate)
        cols = list(range(startIndex,endIndex+1))
        cols = [1,2]+cols[::interval]
        return self.dataDF.iloc[:,[cols]]

    def getColumnIndex(self,columnName):
        return self.dataDF.columns.get_loc(columnName)