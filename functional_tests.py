from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
class NewVisitorTest(unittest.TestCase):

  def setUp(self):
      self.browser = webdriver.Firefox()

  def tearDown(self):
      time.sleep(5)
      self.browser.quit()

 
  # Bob has heard about web application 'Vote'.
  # He goes to check out its homepage
  # nut saw the title name 'Vote'
  def test_can_start_a_list_and_retrieve_it_later(self):
      self.browser.get('http://localhost:8000')
      self.assertIn('Question--Homepage', self.browser.title)

    # Bob เห็นปุ่มตั้งคำถาม
      create_quiz_button = self.browser.find_element_by_name('create_question')
      self.assertEqual(create_quiz_button.get_attribute('value'),
          'Create Question')
      time.sleep(3)
    # Bob กดปุ่มตั้งคำถาม
      create_quiz_button.click()

    # เมื่อกดปุ่มตั้งคำถามเสร็จ จะเปลี่ยนจากหน้า homepage ไปที่หน้าตั้งคำถาม
      check_url_createQuiz = self.browser.current_url
      self.assertRegex(check_url_createQuiz, '/create/')
      time.sleep(3)
    # Bob เห็นช่องสำหับใส่คำถามและ choice 'true', 'false' และปุ่ม Submit
      input_quiz = self.browser.find_element_by_name('name_quiz')
      self.assertEqual(input_quiz.get_attribute('placeholder'), 'Enter a question')

      select_true_choice = self.browser.find_element_by_id('true')
      self.assertEqual(select_true_choice.get_attribute('value'), 'True')
      
      select_false_choice = self.browser.find_element_by_id('false')
      self.assertEqual(select_false_choice.get_attribute('value'), 'False')
      
      submit_quiz_button = self.browser.find_element_by_name('sub_bt')
      self.assertEqual(submit_quiz_button.get_attribute('value'), 'Submit')
      time.sleep(3)
    # Bob ใส่คำถามว่า "นกมีเขา?" และเลือกคำตอบที่ถูกต้องเป็น "False"
      input_quiz.send_keys('นกมีเขา?')
      select_false_choice.click()
      time.sleep(3)

      submit_quiz_button.click()
    
    # หลังจากตั้งคำถามเสร็จจะเปลี่ยนกลับไปที่หน้า homepage
      check_url_homepage_after_createQuiz = self.browser.current_url
      self.assertRegex(check_url_homepage_after_createQuiz, '/')
      time.sleep(2)
    # จะเห็นคำถามที่พึ่งตั้งไปเพิ่มขึ้นมา
      show_quiz = self.browser.find_element_by_link_text('นกมีเขา?')
      show_quiz.click()

    # หลังจากกดที่คำถามจะเปลี่ยนไปที่หน้าที่ใหเโหวตคำตอบ
      check_url_detail = self.browser.current_url
      self.assertRegex(check_url_detail, '/1/')
    # เห็น title 'Detail'
      self.assertIn('Detail', self.browser.title)
      time.sleep(2)
    # เลือก choice 'False'
      select_false_answer = self.browser.find_element_by_id('choice2')
      select_false_answer.click()
      time.sleep(2)
    # กดปุ่ม vote
      vote_button = self.browser.find_element_by_name('vote_bt')
      self.assertEqual(vote_button.get_attribute('value'), 'Vote')
      vote_button.click()

    # หลังจากกดโหวต จะเปลี่ยนไปที่หน้าแสดงผงโหวต
      check_url_result = self.browser.current_url
      self.assertRegex(check_url_result, '/1/results/')
    # เห็น title 'Result'
      self.assertIn('Result',self.browser.title)
      time.sleep(5)
    # จะเห็นลิ้งค์สำหรับกลับไปโหวตใหม่อีกครั้ง
      link_to_vote_again = self.browser.find_element_by_link_text('Vote again')
    # กดเพื่อกลับไปโหวตใหม่
      link_to_vote_again.click()


    # จะเห็นว่ากลับมาที่หน้าสำหรับโหวตอีกครั้ง
      check_url_detail = self.browser.current_url
      self.assertRegex(check_url_detail, '/1/')
    # เห็น title 'Detail'
      self.assertIn('Detail', self.browser.title)
      time.sleep(2)
    # เลือก choice 'True'
      select_false_answer = self.browser.find_element_by_id('choice1')
      select_false_answer.click()
      time.sleep(2)
    # กดปุ่ม vote
      vote_button = self.browser.find_element_by_name('vote_bt')
      self.assertEqual(vote_button.get_attribute('value'), 'Vote')
      vote_button.click()

    # หลังจากกดโหวต จะเปลี่ยนไปที่หน้าแสดงผงโหวต
      check_url_result = self.browser.current_url
      self.assertRegex(check_url_result, '/1/results/')
    # เห็น title 'Result'
      self.assertIn('Result',self.browser.title)
      time.sleep(5)
    # กดกลับไปที่หน้า homepage
      link_to_homepage = self.browser.find_element_by_link_text('Back to home page')
      link_to_homepage.click()
    # เช็คว่าสามารถกลับไปที่หน้า homepage ได้จริงๆ
      check_url_homepage_after_click_link = self.browser.current_url
      self.assertRegex(check_url_homepage_after_click_link, '/')
      time.sleep(3)

      self.fail('Finish the test!')

if __name__ == '__main__':
     unittest.main(warnings='ignore')
