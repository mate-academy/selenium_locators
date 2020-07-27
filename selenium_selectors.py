# Add couple selenium tests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
running_program = 1


# 1. Submit filled test form
# https://demoqa.com/text-box

def text_box():
    TEST_DATA = {
        'username': 'gooddmas',
        'email': 'up2dmas@gmail.com',
        'address': 'My address is not the house, not even the street, my address is USSR'
    }

    browser = webdriver.Chrome()
    browser.get("https://demoqa.com/text-box")
    browser.find_element_by_css_selector('#userName').send_keys(TEST_DATA['username'])
    browser.find_element_by_css_selector('#userEmail').send_keys(TEST_DATA['email'])
    browser.find_element_by_css_selector('#currentAddress').send_keys(TEST_DATA['address'])
    browser.find_element_by_css_selector('#permanentAddress').send_keys(TEST_DATA['address'])
    browser.find_element_by_css_selector('#submit').click()
    print('=== FIRST CASE ENDED ===')
    browser.quit()


# 2. Click on [Code in it] button after selecting new Category
# https://testpages.herokuapp.com/styled/basic-ajax-test.html

def basic_ajax_test():
    browser = webdriver.Chrome()
    browser.get("https://testpages.herokuapp.com/styled/basic-ajax-test.html")
    category_list = Select(browser.find_element_by_css_selector('#combo1'))
    category_list.select_by_value('2')
    sleep(5)
    browser.find_element_by_css_selector('body > div > div.centered > form > input.styled-click-button').click()
    print('=== SECOND CASE ENDED ===')
    browser.quit()


# 3. Print all text in Lorem/Ipsum/Dolor columns
# https://the-internet.herokuapp.com/challenging_dom#delete

def challenging_dom():
    browser = webdriver.Chrome()
    browser.get("https://the-internet.herokuapp.com/challenging_dom#delete")
    # whole_table = browser.find_element_by_xpath('//tbody')
    table = browser.find_element_by_css_selector('#content > div > div > div > div.large-10.columns > table > tbody')
    rows = table.find_elements_by_tag_name('tr')
    for row in rows:
        cols = row.find_elements_by_tag_name('td')
        for col in cols[:3]:
            print(col.text)
    print('=== THIRD CASE ENDED ===')
    browser.quit()


if running_program == 1:
    text_box()
    basic_ajax_test()
    challenging_dom()
    if SystemExit.code != 0:
        print('\nRESULT: All 3 CASES SUCCESSFULLY PASSED')
    else:
        print('There was an error occured.')
