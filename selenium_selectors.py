from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box");
input_field = {
    'Full Name': 'YuraOMG',
    'Email': 'YuraOMG@gmail.com',
    'Current Address': 'Mars',
    'Permanent Address': 'Pluto'
}

driver.find_element_by_xpath('//*[@id="userName"]').send_keys(input_field['Full Name'])
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="userEmail"]').send_keys(input_field['Email'])
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="currentAddress"]').send_keys(input_field['Current Address'])
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="permanentAddress"]').send_keys(input_field['Permanent Address'])
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="submit"]').click()   #here i Have Error!!!!, Traceback (most recent call last):
                                                           #File "/usr/local/bin/selenium_locators/selenium_selectors.py", line 32, in <module>
                                                           #driver.find_element_by_xpath('//*[@id="submit"]').click()
driver.quit()

#================Second
#driver = webdriver.Chrome()
#driver.get("https://testpages.herokuapp.com/styled/basic-ajax-test.html");
#driver.find_element_by_xpath('//*[@id="combo1"]').click()
#driver.find_element_by_xpath('//*[@id="combo1"]/option[2]').click()
#driver.implicitly_wait(2)
#driver.find_element_by_xpath('/html/body/div/div[3]/form/input[1]').click()
#driver.quit()

