from django.template.defaulttags import url

from . import views
from django.urls import path

app_name ='createQuiz'

urlpatterns =[
    path('menu', views.HomeView.as_view(), name='main_menu'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.LogOut.as_view(), name='logout'),
    path('registerForm', views.RegisterStudent.as_view(), name='add_student'),
    path('teacherRegisterForm', views.RegisterTeacher.as_view(), name='add_teacher'),
    path('addQuizForms', views.CreateQuiz.as_view(), name='add_quiz'),
    path('editQuestion', views.EditQuestion.as_view(), name='edit_quiz'),
    path('edit/<int:questionid>', views.EditQuestion.editquiz),
    path('delete/<int:questionid>', views.EditQuestion.delete, name='delete'),
    path('edit/update/<int:questionid>', views.EditQuestion.updatequiz, name='update'),
    path('delete/<int:questionid>', views.EditQuestion.delete, name='delete'),
    path('closeQuiz', views.CloseQuiz.as_view(), name='close_quiz'),
    path('answerQuiz', views.AnswerQuiz.as_view(), name='ans_quiz'),
    path('quizResult', views.QuizResult.as_view(), name='quiz_result'),
    path('addFromQuizBank', views.QuizBank.as_view(), name='quiz_bank'),



]