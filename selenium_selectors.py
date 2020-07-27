"""
Add couple selenium tests
1. Submit filled test form 
https://demoqa.com/text-box
2. Click on [Code in it] button after selecting new Category 
https://testpages.herokuapp.com/styled/basic-ajax-test.html
3. Print all text in Lorem/Ipsum/Dolor columns 
https://the-internet.herokuapp.com/challenging_dom#delete
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestSelectors(unittest.TestCase):
    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("headless")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_submit_form(self):
        driver = self.driver
        driver.get('https://demoqa.com/text-box')
        driver.find_element(By.ID, 'userName').send_keys('Andrii Moisieiev')
        driver.find_element(By.ID, 'userEmail').send_keys('andriitest@gmail.com')
        driver.find_element(By.ID, 'currentAddress').send_keys('Address 1')
        driver.find_element(By.ID, 'permanentAddress').send_keys('Address 2')
        driver.execute_script('document.getElementById("submit").click()') # because of element interception I use js selector
        # driver.find_element(By.ID, 'submit').click()
        self.assertTrue(driver.find_element(By.ID, 'output').is_displayed())

    def test_AJSX_load(self):
        driver = self.driver
        driver.get('https://testpages.herokuapp.com/styled/basic-ajax-test.html')
        driver.find_element(By.XPATH, '//*[@id="combo1"]/option[2]').click()
        driver.find_element(By.XPATH, '//*[@id="combo2"]/option[3]').click()
        driver.find_element(By.CLASS_NAME, 'styled-click-button').click()
        self.assertEqual(driver.current_url, 'https://testpages.herokuapp.com/styled/the_form_processor.php?ajax=1')

    def test_print_text(self):
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/challenging_dom#delete')
        for rows in driver.find_elements_by_xpath("//tbody//tr[//td[contains(., 'Iuvaret')]]"):
            for first_three_col in rows.text.split(' ')[:3]:
                print(first_three_col)


if __name__ == '__main__':
    unittest.main()
