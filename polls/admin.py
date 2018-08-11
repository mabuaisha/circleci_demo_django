import django.contrib.admin

from .models import Question
from .models import Choice


@django.contrib.admin.register(Question)
class QuestionAdmin(django.contrib.admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')


@django.contrib.admin.register(Choice)
class ChoiceAdmin(django.contrib.admin.ModelAdmin):
    fields = ['question', 'choice_text', 'votes']
    list_display = ('question', 'choice_text', 'votes')
