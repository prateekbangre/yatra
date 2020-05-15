import unittest
from helpers.driver import driver
import time

class MyTestCase(unittest.TestCase):
    def testName(self):
      xpath= driver.find_element_by_xpath
      driver.get("https://www.google.com")
      driver.maximize_window()
      driver.delete_all_cookies()
      time.sleep(2)
      search_box = xpath("//input[contains(@class,'gLFyf gsfi')]")
      search_box.send_keys("https://yatra.com")
      search_box.submit()
      xpath('//h3[contains(text(),"Yatra.com:")]').click()
      time.sleep(2)

if __name__ == '__main__':
  MyTestCase.testName()
