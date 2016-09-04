from django.test import TestCase
import datetime
from django.utils import timemzone
from django.urls import reverse

from .models import Question
# Create your tests here.

class QuestionMethodTests(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        """was_published_recently() should return false when date is in the future"""

        time = timezone.now() +  datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertFalse(future_question.was_published_recently(), False)

    def test_was_published_with_old_question(self):
        """was_published_recently() should return false when date is older than one day"""

        time = timeszone.now() - datetime.timedelta(days=1)
        old_question = Question(pub_date=time)
        self.assertFalse(old_question.was_published_recently(), False)

    def test_was_published_with_recent_question(self):
        """ was_published_recently() should return true whemn date is within a day"""

        time =timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertTrue(recent_question.was_published_recently(),True)

def create_question(question_teext, days):
"""Creates a question with the given text and published days offest from now.
A positive value for days indicates a date in the past, positive for future"""

time = timezone.now() + datetime.timedelta(days =days)
return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionViewTests(TestCase):

    def test_index_view_with_no_questions(self):
        """ Display apporopriate message if no question exists"""
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: Pas'])