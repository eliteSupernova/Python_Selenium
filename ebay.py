import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium import webdriver

base_url='https://www.ebay.com/'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(base_url)
# driver.implicitly_wait(10)
driver.execute_script("window.scrollTo(0,1000)")
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="destinations_list1"]//ul//li[4]//a//div[1]//div//div').click()
driver.execute_script("window.scrollTo(0,1100)")
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="s0-27_2-9-0-1[0]-0-0"]/ul/li[2]/div').click()
driver.window_handles[1]
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="mainContent"]//form//div[2]//div//div[1]//div[2]//ul//li[1]//s//div').click()
# time.sleep(5)

# driver.find_element(By.PARTIAL_LINK_TEXT,'Fashion').click()
# time.sleep(4)