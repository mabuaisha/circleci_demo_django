import django.urls

from . import views

urlpatterns = [
    django.urls.path('', views.index, name='index'),
    django.urls.path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    django.urls.path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    django.urls.path('<int:question_id>/vote/', views.vote, name='vote'),
]
