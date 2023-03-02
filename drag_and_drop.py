import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()
base_url='https://www.globalsqa.com/demo-site/draganddrop/'

driver.get(base_url)
driver.maximize_window()
time.sleep(2)

action = ActionChains(driver)
iframe=driver.find_element(By.XPATH,'//*[@id="post-2669"]//div[2]//div//div//div[1]//p//iframe')
driver.switch_to.frame(iframe)
source=driver.find_element(By.XPATH,'//*[@id="gallery"]//li[1]')
target=driver.find_element(By.ID,'trash')
action.drag_and_drop(source,target).perform()
time.sleep(2)


# driver.maximize_window()
# driver.get(base_url)

# drag('//*[@id="gallery"]/li[1]','trash')
time.sleep(3)