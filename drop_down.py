import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium import webdriver

driver = webdriver.Chrome()

base_url='https://guru99.click/MObhE'
driver.get(base_url)
x=driver.find_element(By.XPATH,'//html//body//div[2]//table//tbody/tr//td[2]//table//tbody//tr[4]//td//table//tbody//tr//td[2]//table//tbody//tr[5]//td//form//table//tbody//tr[11]//td[2]//select')
drop=Select(x)
drop.select_by_visible_text("ANTARCTICA")
time.sleep(1)
drop.select_by_index(4)
time.sleep(1)
drop.select_by_value('COOK ISLANDS')
time.sleep(1)
for index in range(0,80):
    drop.select_by_index(index)

time.sleep(5)