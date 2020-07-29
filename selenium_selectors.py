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
import time
from selenium.webdriver.support.ui import Select

def test1():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")
    driver.find_element_by_css_selector('#userName').send_keys("Arnold")
    driver.find_element_by_css_selector('#userEmail').send_keys("Shwarcneger@aa.ua")
    driver.find_element_by_css_selector('#currentAddress').send_keys("USA")
    driver.find_element_by_css_selector('#permanentAddress').send_keys("California")
    driver.find_element_by_css_selector('#submit').click()
    time.sleep(3)
    driver.quit()


test1()

def test2():
    driver = webdriver.Chrome()
    driver.get("https://testpages.herokuapp.com/styled/basic-ajax-test.html")
    driver.implicitly_wait(10)
    select = Select(driver.find_element_by_css_selector('#combo1'))
    select.select_by_index(2)
    driver.find_element_by_css_selector('[class="styled-click-button"]').click()
    time.sleep(3)
    driver.quit()

test2()



def test3():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/challenging_dom#delete")
    lorem_ipsum_dolor = driver.find_elements_by_css_selector('tbody tr')
    for row in lorem_ipsum_dolor:
        print(row.find_element_by_css_selector('td:nth-child(1)').text)

    for row in lorem_ipsum_dolor:
        print(row.find_element_by_css_selector('td:nth-child(2)').text)

    for row in lorem_ipsum_dolor:
        print(row.find_element_by_css_selector('td:nth-child(3)').text)

    driver.quit()


test3()
