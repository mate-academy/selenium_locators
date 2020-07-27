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
from time import sleep

def demoqa(full_name, email, adress_current, adress_perm): #args only stings
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/text-box')

    name_field = driver.find_element_by_css_selector('#userName')
    name_field.send_keys(full_name)
    email_field = driver.find_element_by_css_selector('#userEmail')
    email_field.send_keys(email)
    submit_btn = driver.find_element_by_css_selector('#submit')
    adress_cur_field = driver.find_element_by_css_selector('#currentAddress')
    adress_cur_field.send_keys(adress_current)
    adress_cur_field = driver.find_element_by_css_selector('#permanentAddress')
    adress_cur_field.send_keys(adress_perm)
    submit_btn.click()
    assert full_name in driver.page_source
    assert email in driver.page_source
    assert adress_current in driver.page_source
    assert adress_perm in driver.page_source
    sleep(3)
    driver.quit()


demoqa('some_name', '123@123.com', 'some_addr1', 'some_addr2')

def testpages():
    driver = webdriver.Chrome()
    driver.get('https://testpages.herokuapp.com/styled/basic-ajax-test.html')
    sleep(1)
    new_cat_pick = driver.find_element_by_css_selector('#combo1 > option:nth-child(2)')
    new_cat_pick.click()
    sleep(2)
    driver.implicitly_wait(5)
    submit_btn = driver.find_element_by_xpath('/html/body/div/div[3]/form/input[1]')
    submit_btn.click()
    driver.quit()
testpages()

def herokuapp():
    driver = webdriver.Chrome()
    driver.get('https://the-internet.herokuapp.com/challenging_dom#delete')

    columns = driver.find_elements_by_css_selector('tbody tr')
    for lorem_row in columns:
        print(lorem_row.find_element_by_css_selector('td:nth-child(1)').text)
    print('--------------\n--------------')
    for ipsum_row in columns:
        print(ipsum_row.find_element_by_css_selector('td:nth-child(2)').text)
    print('--------------\n--------------')
    for dolor in columns:
        print(dolor.find_element_by_css_selector('td:nth-child(3)').text)
    driver.quit()
herokuapp()







