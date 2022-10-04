from . import views
from django.urls import path

app_name ='createQuiz'

urlpatterns =[
    path('createQuizForms', views.CreateQuiz.as_view(), name='create_quiz'), #127.0.0.1/registration/createstudent
    path('answerQuiz', views.AnswerQuiz.as_view(), name='ans_quiz'),
    path('quizResult', views.QuizResult.as_view(), name='quiz_result'),

]