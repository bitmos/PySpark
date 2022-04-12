from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
import pandas as pd
from pyspark.sql.functions import col, when
class Model:
    def __init__(self):
        # self.csv=csv
        spark=SparkSession.builder.appName("Analysis").getOrCreate()
        self.df_ResultData=spark.read.csv("/home/bitmos/Documents/GitHub/PySpark/DesktopApp/Results_Data.csv",header=True,inferSchema=True)

    def Objective1(self,subname):
        self.subname=subname
        valueWhenTrue = "F"  # for example

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
        plt.title('Bar plot of Total Score against Number of students')
        plt.xlabel('Total Marks')
        plt.ylabel('Number Of Students')
        df_BySub=self.df_ResultData.filter(self.df_ResultData.SCODE == subname)
        x=df_BySub.toPandas()["TOT"].values.tolist()
        plt.hist(x,rwidth=0.8)
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