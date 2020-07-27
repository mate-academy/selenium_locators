"""
Add couple selenium tests
1. Submit filled test form 
https://demoqa.com/text-box
2. Click on [Code in it] button after selecting new Category 
https://testpages.herokuapp.com/styled/basic-ajax-test.html
3. Print all text in Lorem/Ipsum/Dolor columns 
https://the-internet.herokuapp.com/challenging_dom#delete
"""
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:/selenium/chromedriver.exe")
driver.set_window_size(1920, 1080)
driver.get("https://demoqa.com/text-box")
driver.find_element_by_css_selector(
    '#userForm div:nth-child(1) div:nth-child(2) > input[placeholder=\'Full Name\']').send_keys("Dima")
driver.find_element_by_css_selector(
    '#userForm div:nth-child(2) div:nth-child(2) > input[placeholder=\'name@example.com\']').send_keys(
    "dimalitvin192.0@gmail.com")
driver.find_element_by_css_selector(
    '#userForm div:nth-child(3) div:nth-child(2) > textarea[placeholder=\'Current Address\']').send_keys(
    "Kiev Sechenova 10")
driver.find_element_by_css_selector('#userForm div:nth-child(4) div:nth-child(2) > textarea').send_keys(
    "Kiev Sechenova 10")
driver.find_element_by_css_selector('#userForm div:nth-child(5) div:nth-child(1) > button[id =\'submit\']').click();

assert driver.find_element_by_css_selector('#userForm div:nth-child(6) > div > p:nth-child(1)').text.split(':')[
           1] == 'Dima'
assert driver.find_element_by_css_selector('#userForm div:nth-child(6) > div > p:nth-child(2)').text.split(':')[
           1] == 'dimalitvin192.0@gmail.com'
assert driver.find_element_by_css_selector('#userForm div:nth-child(6) > div > p:nth-child(3)').text.split(':')[
           1] == 'Kiev Sechenova 10'
assert driver.find_element_by_css_selector('#userForm div:nth-child(6) > div > p:nth-child(4)').text.split(':')[
           1] == 'Kiev Sechenova 10'

driver.get("https://testpages.herokuapp.com/styled/basic-ajax-test.html")
elements = driver.find_elements_by_css_selector('form div:nth-child(1) > select[id=\'combo1\'] > option')
for element in elements:
    if element.text == 'Desktop':
        element.click();
        sleep(3)
        button = driver.find_element_by_css_selector('form  > input[value=\'Code In It\']')
        button.click();
        break;

driver.get("https://the-internet.herokuapp.com/challenging_dom#delete")
table = driver.find_elements_by_css_selector('table > tbody > tr');
for row in table:
   cells = row.find_elements_by_css_selector('td');
   i = 0;
   for cell in cells:
       if i > 2:
           break;
       print(cell.text + " "),
       i += 1;
   print ("")