import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException

class MyTestCase(unittest.TestCase):
    def testName(self):
      chrome_options = webdriver.ChromeOptions()
      prefs = {"profile.default_content_setting_values.notifications" : 1}
      chrome_options.add_experimental_option("prefs",prefs)
      driver = webdriver.Chrome(chrome_options=chrome_options , executable_path=r'C:/chromedriver.exe')
      # driver = webdriver.Chrome("C:/chromedriver.exe")
      xpath= driver.find_element_by_xpath
      xpath= driver.find_element_by_xpath
      action = ActionChains(driver)
      #passing the link to the chrome driver
      driver.get("https://www.google.com")
      driver.maximize_window()
      search_box = xpath("//input[contains(@class,'gLFyf gsfi')]")
      search_box.send_keys("https://yatra.com")
      search_box.submit()
      driver.find_element_by_xpath('//h3[contains(text(),"Yatra.com:")]').click()
      time.sleep(2)

if __name__ == '__main__':
 unittest.main()