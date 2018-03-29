from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    time.sleep(10)
    self.browser.quit()

 
  # Nut has heard about web application 'Vote'.
  # He goes to check out its homepage
  # nut saw the title name 'Vote'
  def test_can_start_a_list_and_retrieve_it_later(self):
    self.browser.get('http://localhost:8000')
    self.assertIn('Vote', self.browser.title)
    
    self.fail('Finish the test!')

if __name__ == '__main__':
   unittest.main(warnings='ignore')
