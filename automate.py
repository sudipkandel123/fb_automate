# import psycopg2

# conn = psycopg2.connect(database = "test", user = "sudip", password = "New@1234", host = "127.0.0.1", port = "5432")
# print("Opened database successfully")

# cur = conn.cursor()
# cur.execute("select * from automation.user_data")
# row = cur.fetchall()
# cur.execute(""" SELECT column_name
#   FROM information_schema.columns
#  WHERE table_schema = 'automation'
#    AND table_name   = 'user_data' """)
# cols = cur.fetchall()
# print(cols)
# for i in range(len(row[0])):
#     print(row[0][i])
# cur.close()

import sqlalchemy
import pandas as pd

con = sqlalchemy.create_engine("postgresql://sudip@localhost:5432/test")
df = pd.read_sql_query("select * from automation.user_data",con)
rows = df.values.tolist()
cols = df.columns.tolist()
for i in range(len(rows)):
  user_id = rows[i][2]
  message = rows[i][5]

  print(user_id,message)

#print(len(rows))