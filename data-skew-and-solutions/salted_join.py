# Databricks notebook source
spark.conf.set("spark.databricks.optimizer.adaptive.enabled", "false")
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "-1")

# COMMAND ----------

id_values1 = [1] * 100000 + [2] * 5+ [3] * 5
table1 = spark.createDataFrame (id_values1, "int").toDF("id")
id_values2 = [1] * 100 + [2] * 5+ [3] * 2
table2 = spark.createDataFrame(id_values2, "int").toDF("id")

# COMMAND ----------

display(table1)

# COMMAND ----------

display(table2)

# COMMAND ----------

joined_df = table1.join(table2, on="id", how="left")

# COMMAND ----------

display(joined_df)

# COMMAND ----------

joined_df.explain()

# COMMAND ----------


