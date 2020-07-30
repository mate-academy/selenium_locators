"""
Add couple selenium tests
1. Submit filled test form
https://demoqa.com/text-box
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TEST_DATA = {
        'full_name': 'Test One',
        'email': 'test1@mail.com',
        'cur_address': 'Ukraine',
        'cur_address_two': 'Ukraine'
    }

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.find_element_by_css_selector("#userName").send_keys(TEST_DATA["full_name"])
driver.find_element_by_css_selector("#userEmail").send_keys(TEST_DATA["email"])
driver.find_element_by_css_selector("#currentAddress").send_keys(TEST_DATA["cur_address"])
driver.find_element_by_css_selector("#permanentAddress").send_keys(TEST_DATA["cur_address_two"])
driver.find_element_by_css_selector("#submit").click()
time.sleep(2)
driver.quit()


'''Click on [Code in it] button after selecting new Category
https://testpages.herokuapp.com/styled/basic-ajax-test.html'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()
driver.get("https://testpages.herokuapp.com/styled/basic-ajax-test.html")
l1 = Select(driver.find_element_by_css_selector('#combo1'))
l1.select_by_index(2)
time.sleep(2)
driver.find_element_by_css_selector('.styled-click-button').click()
time.sleep(2)
driver.quit()


""" Print all text in Lorem/Ipsum/Dolor columns
https://the-internet.herokuapp.com/challenging_dom#delete
"""



from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/challenging_dom#delete")
lorem_ipsum_dolor = driver.find_elements_by_css_selector('tbody tr')
for rows in lorem_ipsum_dolor:
    print(rows.find_element_by_css_selector('td:nth-child(1)').text)

for rows in lorem_ipsum_dolor:
    print(rows.find_element_by_css_selector('td:nth-child(2)').text)

for rows in lorem_ipsum_dolor:
    print(rows.find_element_by_css_selector('td:nth-child(3)').text)

driver.quit()

