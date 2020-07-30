# """
# Add couple selenium tests
# 1. Submit filled test form
# https://demoqa.com/text-box
# 2. Click on [Code in it] button after selecting new Category
# https://testpages.herokuapp.com/styled/basic-ajax-test.html
# 3. Print all text in Lorem/Ipsum/Dolor columns
# https://the-internet.herokuapp.com/challenging_dom#delete
# """
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# ----------------------------------------------------------------------------------------------
# 1. Submit filled test form
driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
TEST_DATA = {
    'full_name': 'Maxim',
    'Email': 'maxim@mail.com',
    'Current_address': 'Wall str. 23',
    'Permanent_address': 'Baker str. 12'
}
driver.find_element_by_xpath('//*[@id="userName"]').send_keys(TEST_DATA['full_name'])
driver.find_element_by_xpath('//*[@id="userEmail"]').send_keys(TEST_DATA['Email'])
driver.find_element_by_xpath('//*[@id="currentAddress"]').send_keys(TEST_DATA['Current_address'])
driver.find_element_by_xpath('//*[@id="permanentAddress"]').send_keys(TEST_DATA['Permanent_address'])
driver.find_element_by_xpath('//*[@id="submit"]').click()
assert driver.find_element_by_xpath('//*[@id="output"]')
time.sleep(2)
driver.quit()

# ----------------------------------------------------------------------------------------------
# 2. Click on [Code in it] button after selecting new Category
driver = webdriver.Chrome()
driver.get("https://testpages.herokuapp.com/styled/basic-ajax-test.html")
driver.find_element_by_xpath('//*[@id="combo1"]').click()
driver.find_element_by_xpath('//*[@id="combo1"]/option[3]').click()
driver.find_element_by_xpath('//*[@id="combo2"]').click()
driver.find_element_by_xpath('//*[@id="combo2"]/option[3]').click()
driver.find_element_by_xpath('/html/body/div/div[3]/form/input[1]').click()
time.sleep(2)
assert 'You submitted a form' in driver.page_source
driver.quit()

# ----------------------------------------------------------------------------------------------
# 3. Print all text in Lorem/Ipsum/Dolor columns
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/challenging_dom#delete")
elem = driver.find_elements_by_css_selector('tbody tr')
for row in elem:
    print((row.find_element_by_css_selector('td:nth-child(1)').text),
          (row.find_element_by_css_selector('td:nth-child(2)').text),
          (row.find_element_by_css_selector('td:nth-child(3)').text))
driver.quit()

