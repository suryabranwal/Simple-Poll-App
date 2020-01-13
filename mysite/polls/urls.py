from django.urls import path
from . import  views

app_name = 'polls' #<--like this!
urlpatterns = [
    path('', views.index, name="index"),
    #127.0.0.1:8000/polls/
    path('<int:question_id>/', views.detail, name="detail"),
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),
    #127.0.0.1:8000/polls/2
    path('<int:question_id>/result/', views.result, name="result"),
    #url(r'^(?P<question_id>[0-9]+)/result$', views.results, name="result"),
    # 127.0.0.1:8000/polls/2/result
    path('<int:question_id>/vote/', views.vote, name="vote"),
    #url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name="vote"),
    # 127.0.0.1:8000/polls/2/vote

]