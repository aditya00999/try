from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# import re

if __name__ == '__main__':
    # Create a Spark session
    spark = SparkSession.builder \
        .appName("Oracle") \
        .config("spark.driver.extraClassPath", r"C:\Jar_Files\ojdbc8.jar") \
        .getOrCreate()
    print(spark)

    print("hello")

