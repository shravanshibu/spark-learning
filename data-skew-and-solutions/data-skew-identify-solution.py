# Databricks notebook source
# MAGIC %md
# MAGIC ## Data Skew
# MAGIC Spark has data loaded into memory in the form of partitions. Ideally, the data in the partitions should be uniformly distributed. Data skew is when one or some partitions have significantly more data compared to other partitions. 
# MAGIC
# MAGIC ##But why is it so bad? 
# MAGIC It depends on the extent of the data-skew, but if one or more partitions have significantly more data that the rest, the result can be performance bottlenecks, and wastage of resources. It can cause the following problems:
# MAGIC ##### Straggling tasks
# MAGIC ##### Spills to Disk and Out of Memory errors
# MAGIC

# COMMAND ----------

# Reference: https://medium.com/@suffyan.asad1/handling-data-skew-in-apache-spark-techniques-tips-and-tricks-to-improve-performance-e2934b00b021#:~:text=Data%20skew%20is%20when%20one,and%20grouping%20(%20GroupBy%20)%20operations.

# COMMAND ----------


