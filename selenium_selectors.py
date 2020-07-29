"""Add couple selenium tests"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""1. Submit filled test form
https://demoqa.com/text-box"""
# TEST_DATA = {
#             'Full Name': 'JamesBond',
#             'Email': 'SuperOriginEmail@gmail.com',
#             'Current Address': 'LoL',
#             'Permananet Address': 'lOl'
# }
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/text-box")
# time.sleep(2)
#
# driver.find_element_by_xpath('//*[@id="userName"]').send_keys(TEST_DATA['Full Name'])
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="userEmail"]').send_keys(TEST_DATA['Email'])
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="currentAddress"]').send_keys(TEST_DATA['Current Address'])
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="permanentAddress"]').send_keys(TEST_DATA['Permananet Address'])
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="submit"]').click()
# time.sleep(1)
#
# assert driver.find_element_by_xpath('//*[@id="output"]')
# time.sleep(1)
#
# driver.quit()


"""2. Click on [Code in it] button after selecting new Category
https://testpages.herokuapp.com/styled/basic-ajax-test.html"""
# driver = webdriver.Chrome()
# driver.get("https://testpages.herokuapp.com/styled/basic-ajax-test.html")
# time.sleep(2)
#
# driver.find_element_by_xpath('//*[@id="combo1"]').click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="combo1"]/option[3]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="combo2"]').click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="combo2"]/option[3]').click()
# time.sleep(2)
# driver.find_element_by_xpath('/html/body/div/div[3]/form/input[1]').click()
# time.sleep(2)

# assert 'You submitted a form' in driver.page_source
# time.sleep(2)

# driver.quit()


"""3. Print all text in Lorem/Ipsum/Dolor columns
https://the-internet.herokuapp.com/challenging_dom#delete
"""
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/challenging_dom#delete")
# time.sleep(2)
#
# elems = driver.find_elements_by_css_selector('tbody tr')
# for row in elems:
#     print((row.find_element_by_css_selector('td:nth-child(1)').text), (row.find_element_by_css_selector('td:nth-child(2)').text), (row.find_element_by_css_selector('td:nth-child(3)').text))
# time.sleep(2)
#
# driver.quit()


