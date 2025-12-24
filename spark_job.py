from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SimpleJob") \
    .getOrCreate()

df = spark.read.csv("data/sample.csv", header=True)
print(df.count())

spark.stop()
