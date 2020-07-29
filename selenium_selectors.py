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
    'Full Name': 'Oleksii Samoilenko',
    'Email': 'shithedead@gmail.com',
    'Current Address': 'Kharkiv',
    'Current Address2': 'Kharkiv'
}
driver = webdriver.Chrome()
driver.get('https://demoqa.com/text-box')
time.sleep(2)
driver.find_element_by_css_selector('#userName').send_keys(TEST_DATA['Full Name'])
driver.find_element_by_css_selector('#userEmail').send_keys(TEST_DATA['Email'])
driver.find_element_by_css_selector('#currentAddress').send_keys(TEST_DATA['Current Address'])
driver.find_element_by_css_selector('#permanentAddress').send_keys(TEST_DATA['Current Address2'])
driver.find_element_by_css_selector('#submit').click()
time.sleep(2)
print('hello')
driver.quit()


driver = webdriver.Chrome()
driver.get('https://testpages.herokuapp.com/styled/basic-ajax-test.html')
time.sleep(2)
driver.find_element_by_css_selector('#combo1').click()
driver.find_element_by_css_selector('#combo1 > option:nth-child(2)').click()
time.sleep(3)
driver.find_element_by_css_selector('.styled-click-button').click()
if 'Submitted Values' in driver.page_source:
    print('It`s me')
    driver.quit()



driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/challenging_dom#delete')
time.sleep(2)
allTable = driver.find_element_by_tag_name('table')
rows = driver.find_element_by_tag_name('tbody')
columnes = rows.find_elements_by_tag_name('tr')
for allRow in columnes:
    threeRows = allRow.find_elements_by_tag_name('td')
    for row in threeRows[:3]:
     print(row.text)
driver.quit()











