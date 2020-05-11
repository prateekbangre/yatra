import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
driver = webdriver.Chrome("C:/chromedriver.exe")
action = ActionChains(driver)
#passing the link to the chrome driver
driver.get("https://www.google.com")
driver.maximize_window()
search_box = driver.find_element_by_xpath("//input[contains(@class,'gLFyf gsfi')]")
search_box.send_keys("yatra.com")
search_box.submit()
driver.find_element_by_xpath('//h3[contains(text(),"Yatra.com:")]').click()

if __name__ == '__main__':
     unittest.main()