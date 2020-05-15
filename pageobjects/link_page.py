import unittest
# from lib2to3.pgen2 import driver

#from selenium import webdriver as driver
from testcases.smoke import homePageTests


class TestCase(unittest.TestCase):
    def test_thing(self):
         self.assertEqual(True, True)
    #     homePageTests.test_something()
    # homePageTests.driver.find_element_by_css_selector("#booking_engine_flights").click()
    # homePageTests.driver.back()
    # homePageTests.driver.find_element_by_css_selector("##booking_engine_hotels").click()
    # homePageTests.driver.back()
    # homePageTests.driver.find_element_by_css_selector("#booking_engine_holidays").click()
    # homePageTests.driver.back()
    # homePageTests.driver.find_element_by_css_selector("#booking_engine_buses").click()
    # homePageTests.driver.back()
    # homePageTests.driver.find_element_by_css_selector("#booking_engine_cruise").click()
    # homePageTests.driver.back()
    # homePageTests.driver.find_element_by_css_selector("#booking_engine_adventures").click()
    # homePageTests.driver.back()
    # more= homePageTests.driver.find_element_by_css_selector(".list-more-tab")
if __name__ == '__main__':
    unittest.main()