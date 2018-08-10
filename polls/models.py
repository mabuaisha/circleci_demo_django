import datetime

import django.db.models
import django.utils.timezone


class Question(django.db.models.Model):
    question_text = django.db.models.CharField(max_length=200)
    pub_date = django.db.models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= django.utils.timezone.now() - datetime.timedelta(days=1)


class Choice(django.db.models.Model):
    question = django.db.models.ForeignKey(Question, on_delete=django.db.models.CASCADE)
    choice_text = django.db.models.CharField(max_length=200)
    votes = django.db.models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
