### TODO : - Sign in.
### TODO :- Follow a user
### TODO :- Unfollow a user
### TODO :- Get a user’s followers
#LIBRARIES 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pass_key

#Global Variables
username = pass_key.email
passwrd = pass_key.password
import sqlalchemy
import pandas as pd

con = sqlalchemy.create_engine("postgresql://sudip@localhost:5432/test")
df = pd.read_sql_query("select * from automation.user_data",con)
rows = df.values.tolist()
cols = df.columns.tolist()


class FacebookBot:
    def __init__(self,email,password):
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.maximize_window
        #Setting chrome web driver by passing the location to the executable path
        #Because executable path is in the same dir
        self.email = email
        self.password = password
    
    def signIn(self):
        
        try:
            self.driver.get('https://www.facebook.com/login') #Go to the link
            time.sleep(2)
            self.driver.find_element_by_css_selector()
            emailInput= self.driver.find_element_by_xpath('//*[@id="email"]') #go to the Username Field
            passInput =  self.driver.find_element_by_xpath('//*[@id="pass"]') # go to the password field
            emailInput.send_keys(self.email) #passing email
            passInput.send_keys(self.password) #passing pass
            time.sleep(3)
            passInput.send_keys(Keys.ENTER)
            time.sleep(2)   
            print("{Sign In Success}")
        except Exception as e:
            print("Exception occured while ERROR :: " + str(e))
            exit()

    def messageId(self):
        for i in range(len(rows)):
            time.sleep(3)
            user_id = rows[i][2]
            message = rows[i][5]
            time.sleep(2)
            self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
            time.sleep(2)
            self.driver.get("https://www.facebook.com/messages/t/"+user_id)
            time.sleep(3)
            inputElement = self.driver.find_element_by_css_selector('div._1mf _1mj')
            time.sleep(3)
            inputElement.send_keys(message)
            time.sleep(1)
            inputElement.send_keys(Keys.ENTER)
            time.sleep(4)
    
    def followWithUsername(self):
        return 0

objFb = FacebookBot(username,passwrd)
objFb.signIn()
objFb.messageId()





