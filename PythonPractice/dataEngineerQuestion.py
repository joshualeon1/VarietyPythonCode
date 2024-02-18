from pyspark.sql import SparkSession
from pyspark.sql.types import *

# Creating a Spark session
spark = SparkSession.builder.appName("pysparkQuestion").getOrCreate()

# Our first table of sample data 'a'
table_a = [("2022-08-01T00:00:00Z", "321a6967f11e2dad6d335e8a", 22.2, 68.2, 994.1),
           ("2022-04-28T05:00:00Z", "4566b4179c680881adb57d8d", 28.4, 76.3, 992),
           ("2022-01-27T16:00:00Z", "02a73851114df0879d630dd0", 29.6, 51.3, 1013.9),
           ("2022-08-01T00:00:00Z", "0c7ecd90693548c95a201c6b", 20.1, 80.3, 992.4),
           ("2022-08-21T13:00:00Z", "482312cd99781756d68258b3", 31.2, 39.6, 990.3),
           ("2022-08-21T13:00:00Z", "4566b4179c680881adb57d8d", 29.4, 45, 1002),
           ("2022-06-07T05:00:00Z", "482312cd99781756d68258b3", 17.1, 36.8, 990.9),
           ("2022-10-20T05:00:00Z", "7652e066be5f7f971475f502", 21.4, 44.7, 1001.8),
           ("2022-02-21T15:00:00Z", "c0651f7b1ea5d6e19b195d82", 16.8, 40.8, 1017.2),
           ("2022-01-03T19:00:00Z", "3e2158e0ad4dd4437b6820ed", 29.5, 63.8, 1012.2)]

# Ints mixed with doubles so have to clean the columns
for i in range(len(table_a)):
    record = list(table_a[i])                                                       # fetch record, convert to list
    record[-1] = float(record[-1])                                                  # update columns
    record[-2] = float(record[-2])
    record[-3] = float(record[-3])
    table_a[i] = tuple(record)                                                      # recast as tuple and insert back into table_a

# Our second table of sample data 'b'
table_b = [("2022-08-01T00:00:00Z", "321a6967f11e2dad6d335e8a", 14.5, "W", 2.8),
           ("2022-08-21T13:00:00Z", "482312cd99781756d68258b3", 2.8, "N", 6.7),
           ("2022-01-27T16:00:00Z", "02a73851114df0879d630dd0", 13.4, "SW", 5.5),
           ("2022-08-01T00:00:00Z", "4566b4179c680881adb57d8d", 10.8, "SW", 8.2),
           ("2022-04-28T05:00:00Z", "0c7ecd90693548c95a201c6b", 18.8, "SE", 5.5),
           ("2022-02-21T15:00:00Z", "4566b4179c680881adb57d8d", 17.6, "E", 9.9),
           ("2022-06-07T05:00:00Z", "482312cd99781756d68258b3", 8.4, "SW", 5),
           ("2022-10-20T05:00:00Z", "7652e066be5f7f971475f502", 2.6, "SW", 8),
           ("2022-01-03T19:00:00Z", "c0651f7b1ea5d6e19b195d82", 15.4, "E", 1.7),
           ("2022-08-21T13:00:00Z", "3e2158e0ad4dd4437b6820ed", 9, "E", 0.3)]

# Ints mixed with doubles so have to clean columns
for i in range(len(table_b)):
    record = list(table_b[i])
    record[-1] = float(record[-1])
    record[-3] = float(record[-3])
    table_b[i] = tuple(record)

# Creating the schema for the two dfs
# "timestamp","sensor_id","temperature","humidity","precipitation"
# "timestamp","sensor_id","wind_speed","wind_direction","precipitation"
columns_a = StructType([StructField("timestamp", StringType(), True),
                        StructField("sensor_id", StringType(), True),
                        StructField("temperature", FloatType(), True),
                        StructField("humidity", FloatType(), True),
                        StructField("pressure", FloatType(), True)])

columns_b = StructType([StructField("timestamp", StringType(), True),
                        StructField("sensor_id", StringType(), True),
                        StructField("wind_speed", FloatType(), True),
                        StructField("wind_direction", StringType(), True),
                        StructField("precipitation", FloatType(), True)])

# creating our dataframes
df_a = spark.createDataFrame(table_a, columns_a)
df_b = spark.createDataFrame(table_b, columns_b)

# Join on 'sensor_id' and 'timestamp'
df_ab = df_a.join(df_b,["sensor_id","timestamp"])

# Output
df_ab.select("temperature","humidity","precipitation").orderBy("timestamp").show()
