from pyspark.sql import SparkSession

spark = (
    SparkSession
    .builder
    .appName("DistributedDataPipeline")
    .master("local[*]")
    .getOrCreate()
)
