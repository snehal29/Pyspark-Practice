'''
You have a PySpark DataFrame with 100 million records. You need to remove duplicate records based on customer_id, keeping the latest record based on updated_at

'''
# Approach : So for this 100 million record i 1st discuss the shuffle and reason and there respective solutions
            # We need to use window function row_number() partition by customer_id and order by desc updated_at after that filter all 1st records and drop rest
# Pattern : Row_number() , OrderBY() , filter() , drop() 
# Solution:
from pyspark.sql import functions as f
from pyspark.sql.window import Window

window_spec = window.partitionBY('customer_id').orderBy(f.col('updated_at').desc())

df_result = (df.withColumn('rank',f.row_number().over(window_spec)
            .filter(f.col('rank')==1)
            .drop('rank'))
