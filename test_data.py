import pandas as pd
import datetime
import numpy as np
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium import webdriver
import logging
logger = logging.getLogger('message')

df = pd.read_csv('C:\\Users\\1003647\\Desktop\\FLASK_API\\test_data.csv')
print(df)
stat=[]
error=[]
resp=[]
driver = webdriver.Chrome()
now=datetime.datetime.now()

base_url = 'https://3i.honohr.com/login'
driver.maximize_window()
# driver.get(base_url)
# driver.find_element(By.NAME,'q').send_keys('HONOHR3i'+Keys.ENTER)
# driver.find_element(By.PARTIAL_LINK_TEXT,"HONOHR Login").click()
for i in range(len(df['username'])):
    print(df['username'][i],df['pass'][i])

for i in range(len(df['username'])):
    t1=datetime.datetime.now()
    print(t1)
    driver.get(base_url)
    driver.implicitly_wait(2)
    driver.find_element(By.ID,'Usernameid').send_keys(str(df['username'][i]))
    driver.find_element(By.NAME,'password').send_keys(str(df['pass'][i]))
    # driver.implicitly_wait(1)
    driver.find_element(By.XPATH,'//html//body//div//div//div//form//div[2]//div[4]//ul//li[1]//span/label').click()
    # time.sleep(2)
    try:
        driver.find_element(By.XPATH, "/html//body//div//div//div//form//div[2]//div[5]//button").click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'//*[@id="ulid"]//li[3]//div//ul//li[3]//a')
    # driver.manage(3)
        # driver.find_element(By.XPATH, "/html/body/div/div/div/form/div[2]/div[5]/button").click()
        # time.sleep(3)
        # driver.refresh()

    except Exception as e:
        # print(repr(e))
        stat.append('test_failed')
        error.append(repr(e))

        # driver.refresh()
    else:
        print('test_pass')
        stat.append('test_pass')
        error.append('None')
    t2=datetime.datetime.now()
    print(t2)
    total=t2-t1
    resp.append(str(total.seconds)+'.'+str(total.microseconds))
    print(resp)

        # driver.refresh()
    # driver.find_element(By.XPATH,'//html//body//div//div//div//form//div[2]//div[4]//ul//li[1]//span/label').click()
    # time.sleep(2)

    # driver.find_element(By.XPATH,"//html//body//div//div//div//form//div[2]//div[5]//button").click()
    # driver.find_element(By.PARTIAL_LINK_TEXT,'Sign in').click()
    # time.sleep(3)
# print(stat)
# print(error)
df['status']=stat
df['Error']=error
df['Response_time']=resp
print(df)