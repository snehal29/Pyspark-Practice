'''
You are provided with a dataset containing customer information. The dataset may have missing values in the customer_id or email columns. Your task is to filter out any rows where either customer_id or email is null.

Input
File Path: /datasets/customers_raw.csv

Schema:

customer_id (double)
name (string)
email (string)
age (int)
Example Table:

customer_id	name	email	age
1	John	john@email.com	30
2	Alice	NULL	25
NULL	Bob	bob@email.com	22
4	Charlie	charlie@email.com	28
Output
Filter out rows with null values in customer_id or email.

Output Schema:

customer_id (double)
name (string)
email (string)
age (int)
Example Output Table:

customer_id	name	email	age
1	John	john@email.com	30
4	Charlie	charlie@email.com	28
Explanation
Rows where either customer_id or email is null have been removed. Use display(df) to show the final DataFrame.
'''
#Approach : read CSV file , use dropna() function with particular column for null value check and drop and display result
# Solution:

# Initialize Spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

#Copy the starter code or load the file path available in the problem statement 
df =spark.read.csv('/datasets/customers_raw.csv',header=True,inferSchema=True)
df_result = df.dropna(subset=['customer_id','email'])
# Display the final DataFrame using the display() function.
display(df_result)
