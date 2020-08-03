"""
Add couple selenium tests
1. Submit filled test form 
https://demoqa.com/text-box
2. Click on [Code in it] button after selecting new Category 
https://testpages.herokuapp.com/styled/basic-ajax-test.html
3. Print all text in Lorem/Ipsum/Dolor columns 
https://the-internet.herokuapp.com/challenging_dom#delete
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TEST_DATA = {
    'Full Name': 'Alexey Kurbetyev',
    'Email': 'alextestemail@gmail.com',
    'Current Adress': 'Kharkiv'
}
url1 = 'https://demoqa.com/text-box'
url2 = 'https://testpages.herokuapp.com/styled/basic-ajax-test.html'
url3 = 'https://the-internet.herokuapp.com/challenging_dom#delete'

driver = webdriver.Chrome()
driver.get(url1)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#userName").send_keys(TEST_DATA['Full Name'])
driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys(TEST_DATA['Email'])
driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys(TEST_DATA['Current Adress'])
driver.find_element(By.CSS_SELECTOR, "#permanentAddress").send_keys(TEST_DATA['Current Adress'])
driver.find_element(By.CSS_SELECTOR, "#submit").click()
driver.quit()
time.sleep(4)

driver = webdriver.Chrome()
driver.get(url2)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#combo1").click()
driver.find_element(By.CSS_SELECTOR, "#combo1 > option:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".styled-click-button").click()
assert 'Processed Form Details' in driver.page_source
driver.quit()
time.sleep(4)

driver = webdriver.Chrome()
driver.get(url3)
table = driver.find_elements(By.CSS_SELECTOR,'tbody tr')
for rows in table:
    print(rows.find_element(By.CSS_SELECTOR,'td:nth-child(1)').text)

for rows in table:
    print(rows.find_element(By.CSS_SELECTOR,'td:nth-child(2)').text)

for rows in table:
    print(rows.find_element(By.CSS_SELECTOR,'td:nth-child(3)').text)
driver.quit()

