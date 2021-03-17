
import dask.dataframe as df

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