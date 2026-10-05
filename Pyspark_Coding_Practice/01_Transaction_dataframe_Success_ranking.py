'''
You have a PySpark DataFrame containing customer transaction data:

customer_id | transaction_date | amount | status
--------------------------------------------------
101         | 2026-09-01       | 500    | SUCCESS
101         | 2026-09-02       | 200    | FAILED
101         | 2026-09-03       | 300    | SUCCESS
102         | 2026-09-01       | 1000   | SUCCESS
102         | 2026-09-02       | 500    | SUCCESS

The requirement is:
For each customer, calculate their total successful transaction amount and rank customers from highest to lowest based on that amount. 
'''

# Approach : Group on customer id and get total amount using SUM() and condition of status == 'Success' after that use Window function dense_rank order by total amount desc to get higher rank 1st and lower last
# Pattern : filter , groupBy , agg(SUM()) , window , dense_rank() , oderBY()  
# Solution:
from pyspark.sql import functions as F
from pyspark.sql.window import Window

df_result = (
    df.filter(F.col("status") == "SUCCESS")
      .groupBy("customer_id")
      .agg(F.sum("amount").alias("total_amount"))
)

window_spec = Window.orderBy(F.col("total_amount").desc())

df_result = (
    df_result
    .withColumn("rank", F.dense_rank().over(window_spec))
    .orderBy(F.col("total_amount").desc())
)
