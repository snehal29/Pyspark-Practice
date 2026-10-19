'''
You need to process a customer dataset to identify high-value customers. Specifically, you will:

Read data from a CSV file with inferSchema option as true.
Filter customers with a purchase amount more than 100 USD.
Further filter to include only customers aged 30 or above.
Use display(df) to show the final DataFrame.
Input
File Path:
/datasets/customers.csv

Schema:

Column	Type
customer_id	integer
name	string
email	string
age	integer
purchase_amount	double
Example Data:

customer_id	name	email	age	purchase_amount
1	Alice Johnson	alice@email.com	25	150.50
2	Bob Smith	bob@email.com	32	200.00
3	Charlie Brown	charlie@email.com	29	75.00
4	Diana Prince	diana@email.com	40	120.00
5	Evan Davis	evan@email.com	35	90.00
Output
Call display function:
Use display(df) to show the final DataFrame. Make sure the schema is correct.

Schema:

Column	Type
customer_id	integer
name	string
purchase_amount	double
Example Data:

customer_id	name	purchase_amount
2	Bob Smith	200.00
4	Diana Prince	120.00
Explanation:

The output DataFrame df_result includes customers who have a purchase amount of at least 100 USD and are aged 30 or above.
In the example, Bob Smith and Diana Prince meet these criteria, so they are included in the result.
'''

# Pyspark solution

#Initialize Spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

#Copy the starter code or load the file path available in the problem statement 
df_result= (spark.read\
           .option("header",True)\
           .option("InferSchema",True)\
           .csv("/datasets/customers.csv "))
df_result = df_result.filter((df_result['purchase_amount'] > 100) & (df_result['age'] >= 30))
df_result = df_result.select('customer_id', 'name', 'age', 'purchase_amount') 
# Display the final DataFrame using the display() function.
display(df_result)
