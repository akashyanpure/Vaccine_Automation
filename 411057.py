import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('./chromedriver')

driver.get("https://www.cowin.gov.in/home")

driver.find_element_by_id("mat-input-0").send_keys("411057" + Keys.ENTER)


driver.find_element_by_class_name("form-check-label").click()

while True:
    time.sleep(3)
    driver.find_element_by_class_name('pin-search-btn').click()
    driver.find_element_by_class_name("form-check-label").click()
