from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
import pandas as pd
from pyspark.sql.functions import col, when
from pyspark.ml.feature import VectorAssembler
import string
from pyspark.ml.classification import RandomForestClassificationModel
from pyspark.ml.regression import LinearRegressionModel



class Model:
    def __init__(self):
        self.spark=SparkSession.builder.appName("Analysis").getOrCreate()
        self.df_ResultData=self.spark.read.csv("Results_Data.csv",header=True,inferSchema=True)

    def replace_all1(self,text, encoded1):
        for i, j in encoded1.items():
            text = text.replace(i, str(j))
        return text

    def encode(self,a,b,c):
        encoded1= {}
        count =0
        for i in string.ascii_uppercase:
            if i not in encoded1:
                encoded1[i]= count
            count = count +1
        data={'encodedUSN':int(self.replace_all1(a,encoded1)),'NEWDATE':c,'SCODEFINAL':b}
        dataframe1 = self.spark.createDataFrame([data])
        featureassembler=VectorAssembler(inputCols=['encodedUSN','NEWDATE','SCODEFINAL'],outputCol="NEW")
        output1=featureassembler.transform(dataframe1)
        testfinal = output1.select('NEW')
        return testfinal

    def Objective1(self,subname):
        plt.title('Bar plot of Total Score against Number of students')
        plt.xlabel('Total Marks')
        plt.ylabel('Number Of Students')
        df_BySub=self.df_ResultData.filter(self.df_ResultData.SCODE == subname)
        x=df_BySub.toPandas()["TOT"].values.tolist()
        plt.hist(x,rwidth=0.8)
        plt.show()
        

    def Objective2(self,data):
        persistedModel = RandomForestClassificationModel.load("/home/bitmos/Documents/GitHub/PySpark/DesktopApp/models")
        predictions = persistedModel.transform(data)
        data_iter=predictions.rdd.toLocalIterator()
        for i in data_iter:
            return i['prediction']


    def Objective3(self,usn):
        df=self.df_ResultData.select('USN','SCODE','TOT','RESULT','ExamType')
        dftry=df.na.drop(how='any',subset='ExamType')
        df1=dftry.filter((dftry.ExamType == 'Regular') & (dftry.RESULT == "F"))
        sub=[]
        flag=[]
        df2=dftry.filter((dftry.ExamType == 'Regular') & (dftry.RESULT == "F") & (dftry.USN == usn))
        df3=dftry.filter((dftry.ExamType == 'Backlog') & (dftry.RESULT == "P") & (dftry.USN == usn))
        for i in df2.select("SCODE").collect():
            sub.append(i['SCODE'])
            if i['SCODE'] in df3.toPandas()["SCODE"].values.tolist():
                flag.append(i['SCODE'])
        return sub,flag


    def Objective4(self,subname):
        self.subname=subname
        valueWhenTrue = "F" 

        df_ResultData=self.df_ResultData.withColumn(
                        "RESULT",
                        when(
                        col("RESULT") == 'A',
                        valueWhenTrue
                        ).otherwise(col("RESULT"))
                        )
        plt.title('Plot of Total Students Passed in a Subject')
        plt.xlabel('Result')
        plt.ylabel('Number Of Students')
        df_BySub=df_ResultData.filter(df_ResultData.SCODE == self.subname)
        x=df_BySub.toPandas()["RESULT"].values.tolist()
        plt.hist(x)
        plt.show()
       

    def Objective5(self,usn):
        dfT = self.df_ResultData.withColumn("DATE", when(self.df_ResultData.DATE == 'Jul-20','2020-Jul')
                                 .when(self.df_ResultData.DATE == '20-Jul','2020-Jul')
                                 .when(self.df_ResultData.DATE == 'Jan-20','2020-Jan')
                                 .when(self.df_ResultData.DATE == '12019','2019-Jan')
                                 .when(self.df_ResultData.DATE == '72019','2019-Jul')
                                 .when(self.df_ResultData.DATE == '12020','2020-Jan')
                                 .when(self.df_ResultData.DATE == '72020','2020-Jul'))
        dftry1=dfT.filter(dfT.USN == usn)
        df_data=dftry1.select('DATE','TOT')
        dfPlot1=df_data.groupBy("DATE").avg("TOT")
        dfPlot=dfPlot1.sort('DATE')
        plt.title('Student Performnace')
        plt.xlabel('Year')
        plt.ylabel('Total Marks')
        x=dfPlot.toPandas()['DATE'].values.tolist()
        y=dfPlot.toPandas()['avg(TOT)'].values.tolist()
        plt.plot(x,y,marker = 'o')
        plt.ylim(0,100)
        plt.show()

    def Objective6(self,data):
        persistedModel = LinearRegressionModel.load("/home/bitmos/Documents/GitHub/PySpark/DesktopApp/model2")
        predictions = persistedModel.transform(data)
        data_iter=predictions.rdd.toLocalIterator()
        for i in data_iter:
            return i['prediction']