from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
import pandas as pd
from pyspark.sql.functions import col, when
class Model:
    def __init__(self,csv):
        self.csv=csv
        spark=SparkSession.builder.appName("Analysis").getOrCreate()
        self.df_ResultData=spark.read.csv(self.csv,header=True,inferSchema=True)

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

    def Objective2(self,subname):
        plt.title('Bar plot of Total Score against Number of students')
        plt.xlabel('Total Marks')
        plt.ylabel('Number Of Students')
        df_BySub=self.df_ResultData.filter(self.df_ResultData.SCODE == subname)
        x=df_BySub.toPandas()["TOT"].values.tolist()
        plt.hist(x,rwidth=0.8)
        plt.show()
