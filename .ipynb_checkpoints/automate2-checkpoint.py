import sqlalchemy
import pandas as pd
con = sqlalchemy.create_engine("postgresql://sudip@localhost:5432/test")
df = pd.read_sql_query("select * from automation.user_data",con)
print(df.iloc(0))