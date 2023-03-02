import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
base_url = 'https://www.google.com/'
driver.maximize_window()
driver.get(base_url)
driver.find_element(By.NAME,'q').send_keys('HONOHR3i'+Keys.ENTER)
driver.find_element(By.PARTIAL_LINK_TEXT,"HONOHR Login").click()
driver.find_element(By.CSS_SELECTOR,'input.username').send_keys('wassup')
# for ele in input_ele:
#     print(ele.get_attribute('id'))
# driver.find_element(By.CSS_SELECTOR,'input.login__input name').send_keys('1003647')
# driver.find_element(By.NAME,'password').send_keys('Justin@78')
# driver.find_element(By.XPATH,'//html//body//div//div//div//form//div[2]//div[4]//ul//li[1]//span/label').click()
# time.sleep(2)
# # driver.find_element(By.XPATH,"//html//body//div//div//div//form//div[2]//div[5]//button").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,'Sign in').click()
# time.sleep(3)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
