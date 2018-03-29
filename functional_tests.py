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

 
  # Bob has heard about web application 'Vote'.
  # He goes to check out its homepage
  # nut saw the title name 'Vote'
  def test_can_start_a_list_and_retrieve_it_later(self):
      self.browser.get('http://localhost:8000')
      self.assertIn('Vote', self.browser.title)

    # Bob เจอช่องสำหรับใส่คำถาม
      input_quiz = self.browser.find_element_by_id('id_quiz')
      self.assertEqual(input_quiz.get_attribute('placeholder'),
          'Enter a question')
    # Bob ใส่คำถาม "ดาวโลกมีสีฟ้า ?"  
      input_quiz.send_keys('ดาวโลกมีสีฟ้า ?')
      time.sleep(2)
    # Bob click "submit"
      submit_bt = self.browser.find_element_by_name('sub_bt')
      submit_bt.click()
      time.sleep(3)
    
      time.sleep(3)
    
      self.fail('Finish the test!')

if __name__ == '__main__':
     unittest.main(warnings='ignore')
