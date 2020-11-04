import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver/chromedriver")
driver.implicitly_wait(3)

driver.get("https://typing.works/")

i = 0

while True:
    time.sleep(0.1)
    text = driver.find_element_by_id('sing').get_attribute("innerHTML")
    ipt = driver.find_element_by_id('ipt')

    ipt.send_keys(text)
    time.sleep(0.1)
    ipt.send_keys(Keys.RETURN)
    i += 1
    time.sleep(0.5)

