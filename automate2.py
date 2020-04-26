## Importing Libraries
import sqlalchemy
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pass_key

class automate2:
    def __init__(self):
        print('{Initiated Program} \n')

    def connect_db(self):
        print("{Inside db} \n")
        con = sqlalchemy.create_engine("postgresql://sudip@localhost:5432/test")
        df = pd.read_sql_query("select * from automation.user_data",con)
        print(df)

    def selenium_automate(self):
        print("{selenium Started} \n")
        driver = webdriver.opera("./")

obj = automate2()
obj.connect_db()
#obj.selenium_automate()