from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from quiz.views import home_page
from quiz.models import Topic, Choice, Answer
# Create your tests here.

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        expected_html = render_to_string('home.html')
        self.assertEqual(html, expected_html)

class TopicModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
#------------------------question1-----------------        
#----------------save data to database------------------        
        frist_quiz = Topic()
        frist_quiz.post_text = 'The first question'
        frist_quiz.save()

        frist_choice = Choice()
        frist_choice.choice_text = 'The first choice'
        frist_choice.votes = '0'
        frist_choice.topic = frist_quiz
        frist_choice.save()

        second_choice = Choice()
        second_choice.choice_text = 'The second choice'
        second_choice.votes = '1'
        second_choice.topic = frist_quiz
        second_choice.save()

        frist_ans = Answer()
        frist_ans.ans_text = 'The first answer'
        frist_ans.ns_vote = '0'
        frist_ans.topic = frist_quiz
        frist_ans.save()

        second_ans = Answer()
        second_ans.ans_text = 'The second answer'
        second_ans.ns_vote = '1'
        second_ans.topic = frist_quiz
        second_ans.save()

#------------------------------------question 2----------------------------------------
#------------------------------------save data to database----------------------------------------        
        second_quiz = Topic()
        second_quiz.post_text = 'the second question'
        second_quiz.save()

        quiz2_frist_choice = Choice()
        quiz2_frist_choice.choice_text = 'The first choice for the second question'
        quiz2_frist_choice.votes = '0'
        quiz2_frist_choice.topic = second_quiz
        quiz2_frist_choice.save()

        quiz2_frist_ans = Answer()
        quiz2_frist_ans.ans_text = 'The first answer for the second question'
        quiz2_frist_ans.ns_vote = '0'
        quiz2_frist_ans.topic = second_quiz
        quiz2_frist_ans.save()


#------------------------------------test object----------------------------------------
        saved_quiz = Topic.objects.all()
        self.assertEqual(saved_quiz.count(),2)

        saved_choice = Choice.objects.all()
        self.assertEqual(saved_choice.count(),3)

        first_saved_quiz = saved_quiz[0]
        second_saved_quiz =saved_quiz[1]
        self.assertEqual(first_saved_quiz.post_text, 'The first question')
        self.assertEqual(second_saved_quiz.post_text, 'the second question')

#--------------------test object question1-----------------
#------------ทดสอบ choice ของ question1 ว่าถูกต้อง---------------
        quiz1 = Topic.objects.get(id='1')

        choice_quiz1 = quiz1.choice_set.all()
        self.assertEqual(choice_quiz1.count(),2)

        first_saved_choice = choice_quiz1[0].choice_text
        second_saved_choice = choice_quiz1[1].choice_text
        self.assertEqual(first_saved_choice, 'The first choice')
        self.assertEqual(second_saved_choice, 'The second choice')
#----------------ทดสอบ answer ของ question1 ว่าถูกต้อง------------------------------
        ans_quiz1 = quiz1.answer_set.all()
        self.assertEqual(ans_quiz1.count(),2)

        first_saved_answer = ans_quiz1[0].ans_text
        second_saved_answer = ans_quiz1[1].ans_text
        self.assertEqual(first_saved_answer, 'The first answer')
        self.assertEqual(second_saved_answer, 'The second answer')

#------------------------------------test object question1----------------------------------------
#-----------------------------ทดสอบ choice ของ question2 ว่าถูกต้อง------------------------------------ 
        quiz2 = Topic.objects.get(id='2')

        choice_quiz2 = quiz2.choice_set.all()
        self.assertEqual(choice_quiz2.count(),1)

        quiz2_first_saved_choice = choice_quiz2[0].choice_text
        self.assertEqual(quiz2_first_saved_choice, 'The first choice for the second question')

#-----------------------------ทดสอบ answer ของ question2 ว่าถูกต้อง--------------------------------
        ans_quiz2 = quiz2.answer_set.all()
        self.assertEqual(ans_quiz2.count(),1)

        quiz2_first_saved_answer = ans_quiz2[0].ans_text
        self.assertEqual(quiz2_first_saved_answer, 'The first answer for the second question')

