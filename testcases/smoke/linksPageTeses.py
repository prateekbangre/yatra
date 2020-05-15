import unittest
from testcases.smoke import homePageTests
from helpers.driver import driver
from homePageTests import MyTestCase
import time

class linkVerification(unittest.TestCase):
 def testName1(self):
     print("finish")
     time.sleep(20)
     driver.find_element_by_css_selector('a[title="Flights"]').click()
     time.sleep(2)
     driver.find_element_by_xpath("//span[contains(text(),'Book Flights, Hotels and Holiday Packages')]").is_displayed()
     driver.find_element_by_css_selector("#booking_engine_hotels").click()
     time.sleep(5)
     driver.find_element_by_css_selector("#booking_engine_holidays").click()
     driver.find_element_by_css_selector("#booking_engine_buses").click()
     driver.back()
     driver.find_element_by_css_selector("#booking_engine_cruise").click()
     driver.back()
     driver.find_element_by_css_selector("#booking_engine_adventures").click()
     # driver.switch_to.window(self)
     time.sleep(5)
     # driver.close()
     # driver.window_handles[0]


     time.sleep(2)
     more= driver.find_element_by_css_selector(".list-more-tab")
     time.sleep(20)
if __name__ == '__main__':
    MyTestCase.testName()
    linkVerification.testName1()
