from pyspark.sql import SparkSession                                # alawys needed to start a Spark session
from pyspark.sql.types import *                                     # may be used to create schemas


# Creating a Spark session
spark = SparkSession.builder.appName("app_name_here").getOrCreate()

# example of a list we can use to create a dataframe
data = [("Joshua","Leon",24),
        ("Connor","Tree",28),
        ("Philipe","Rodriguez",24),
        ("Ivan","Pineda",22),
        ("Anthony","Pineda",24)]

# the schema for the above:
columns = StructType([
    StructField("fname", StringType(), True),
    StructField("lname", StringType(), True),
    StructField("age", IntegerType(), True)])

# data to be used for SQL Table example
sql_data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "Los Angeles"}
]

df_sql = spark.createDataFrame(sql_data)

df_sql.createOrReplaceTempView("people")

query = "SELECT * FROM people WHERE age >= 30"
result_df = spark.sql(query)
result_df.show()

# we can read in the following files as such:
df_csv = spark.read.csv("csv_name_here")
json_file = "path/to/our/json/file.json"
df_json = spark.read.json(json_file)
parquet_file = "path/to/our/parquet/file.parquet"
df_parquet = spark.read.parquet(parquet_file)
df_text = spark.read.text("output.txt")
df_list = spark.createDataFrame(data, columns)                        # <-- data and schema(columns) from above passed

# this prints the schema
df_list.printSchema()

# In this example, we use 'header=True' if the file has a header, and by infering schema, a pass will be done over the columns to set the column types for us
# than manually doing it like on line 16
df_csv2 = spark.read.csv("file_name.csv", header=True, inferSchema=True)

# this prints out the first 3 records from our list
df_list.head(3)

# this is like the 'SELECT' from SQL where you only output the values for the column 'fname', we may also do multiple columns as shown
df_list.select("fname").show()
df_list.select(["fname","lname"])

# this should output the data types of each column being: [('fname','string'),('lname','string'),('age','int')]
df_list.dtypes

# adding a column to the dataframe:
df_list.withColumn("Age after two years", df_list['age']+2).show()

# dropping a column from a dataframe:
df_list = df_list.drop('Age after two years')
df_list.show()

# renaming a column
df_list.withColumnRenamed('fname','first_name').show()

# suppose our csv file had rows with 'null' values, the function below drops any row with null
df_csv.na.drop().show()

