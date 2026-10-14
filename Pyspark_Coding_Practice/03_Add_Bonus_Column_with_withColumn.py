'''
Source: https://pyspark.in/challenges/add-a-bonus-column-with-withcolumn
Add a column bonus equal to 10% of salary (salary * 0.1). Return all three columns as df_result.
Add a bonus column equal to 10% of salary, keeping the existing columns.
Example:
name	salary
Asha	50000
Ravi	62000

Expected Output:
name	salary	bonus
Asha	50000	5000.0
Ravi	62000	6200.0

Solution: 
'''
from pyspark.sql.functions import col
df_result = employees  # TODO: add bonus = salary * 0.1
df_result = df_result.withColumn('bonus', col('SALARY') *0.1)
df_result =df_result.select('NAME','SALARY','bonus')
df_result.show()
