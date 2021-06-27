import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('./chromedriver')

# Redirect to website
driver.get("https://www.cowin.gov.in/home")

# Select district wise search
# driver.find_element_by_class_name('status-switch').click()
# time.sleep(1)
# driver.find_element_by_id("mat-select-value-1").click()
# time.sleep(1)
# driver.find_element_by_id("mat-option-21").click()
# time.sleep(1)
# driver.find_element_by_id('mat-select-2').click()
# time.sleep(1)
# driver.find_element_by_id("mat-option-61").click()
# time.sleep(1)



# driver.find_element_by_class_name('pin-search-btn').click()
# time.sleep(1)

driver.find_element_by_id("mat-input-0").send_keys("411033" + Keys.ENTER)


driver.find_element_by_class_name("form-check-label").click()

while True:
    time.sleep(3)
    driver.find_element_by_class_name('pin-search-btn').click()
    driver.find_element_by_class_name("form-check-label").click()
