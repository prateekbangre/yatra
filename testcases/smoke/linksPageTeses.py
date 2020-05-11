import unittest
from testcases.smoke import homePageTests
from homePageTests import MyTestCase
from selenium import webdriver as driver
from selenium.webdriver.common import desired_capabilities
import time

class TestCase(unittest.TestCase):
 def testName1(self):
     # chrome_options = driver.ChromeOptions()
     MyTestCase.testName(self)
     print("finish")
     # driver.find_element_by_css_selector('a[title="Flights"]').click()
     # time.sleep(2)
     # driver.find_element_by_xpath("//span[contains(text(),'Book Flights, Hotels and Holiday Packages')]").is_displayed()
     # driver.find_element_by_css_selector("#booking_engine_hotels").click()
     # time.sleep(5)
     # driver.find_element_by_css_selector("#booking_engine_holidays").click()
     # driver.find_element_by_css_selector("#booking_engine_buses").click()
     # driver.back()
     # driver.find_element_by_css_selector("#booking_engine_cruise").click()
     # driver.back()
     # driver.find_element_by_css_selector("#booking_engine_adventures").click()
     # driver.back()
     # more= self.driver.find_element_by_css_selector(".list-more-tab")
     # time.sleep(2)
if __name__ == '__main__':
    unittest.main()