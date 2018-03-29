from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from quiz.views import home_page
from quiz.models import Topic
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
        
        frist_quiz = Topic()
        frist_quiz.post_text = 'The first question'
        frist_quiz.save()

        second_quiz = Topic()
        second_quiz.post_text = 'the second question'
        second_quiz.save()

        saved_quiz = Topic.objects.all()
        self.assertEqual(saved_quiz.count(),2)

        first_saved_quiz = saved_quiz[0]
        second_saved_quiz =saved_quiz[1]
        self.assertEqual(first_saved_quiz.post_text, 'The first question')
        self.assertEqual(second_saved_quiz.post_text, 'the second question')

