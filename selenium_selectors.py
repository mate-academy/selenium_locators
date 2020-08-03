"""
Add couple selenium tests
1. Submit filled test form 
https://demoqa.com/text-box
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
TEST_DATA = {
        'full_name': 'Iryna',
        'email': 'test24@gmail.com',
        'current_address': 'Lviv'
    }
driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
time.sleep(3)
driver.find_element_by_css_selector("#userName").send_keys(TEST_DATA["full_name"])
driver.find_element_by_css_selector("#userEmail").send_keys(TEST_DATA["email"])
driver.find_element_by_css_selector("#currentAddress").send_keys(TEST_DATA["current_address"])
driver.find_element_by_css_selector("#permanentAddress").send_keys(TEST_DATA["current_address"])
driver.find_element_by_css_selector("#submit").click()
time.sleep(2)
driver.quit()

2. Click on [Code in it] button after selecting new Category 
https://testpages.herokuapp.com/styled/basic-ajax-test.html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()
driver.get("https://testpages.herokuapp.com/styled/basic-ajax-test.html")
list = Select(driver.find_element_by_css_selector('#combo1'))
list.select_by_value("2")
time.sleep(2)
driver.find_element_by_css_selector('.styled-click-button').click()
time.sleep(2)
driver.quit()

3. Print all text in Lorem/Ipsum/Dolor columns 
https://the-internet.herokuapp.com/challenging_dom#delete
"""
