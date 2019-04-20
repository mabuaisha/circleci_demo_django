import django.test

from ..models import Question
from ..models import Choice


class PollsTestCase(django.test.TestCase):
    fixtures = ('choice.json', 'question.json')

    def test_questions_count(self):
        self.assertEqual(Question.objects.count(), 3)

    def test_choice_count(self):
        self.assertEqual(Choice.objects.count(), 3)

    def test_dummy(self):
        self.assertEqual('2', '2')