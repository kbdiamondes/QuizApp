from django.forms import ModelForm
from django import forms
from .models import Quiz, StudentAnswer, QuizResult


class CreateQuizForm(ModelForm):
    subjectname = forms.CharField(widget=forms.TextInput())
    question1 = forms.CharField(widget=forms.TextInput())
    question2 = forms.CharField(widget=forms.TextInput())
    question3 = forms.CharField(widget=forms.TextInput())
    question4 = forms.CharField(widget=forms.TextInput())
    question5 = forms.CharField(widget=forms.TextInput())
    correctanswer1 = forms.CharField(widget=forms.TextInput())
    correctanswer2 = forms.CharField(widget=forms.TextInput())
    correctanswer3 = forms.CharField(widget=forms.TextInput())
    correctanswer4 = forms.CharField(widget=forms.TextInput())
    correctanswer5 = forms.CharField(widget=forms.TextInput())
    eqpoints1 = forms.CharField(widget=forms.TextInput())
    eqpoints2 = forms.CharField(widget=forms.TextInput())
    eqpoints3 = forms.CharField(widget=forms.TextInput())
    eqpoints4 = forms.CharField(widget=forms.TextInput())
    eqpoints5 = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Quiz
        fields = ['subjectname', 'question1', 'question2', 'question3', 'question4', 'question5', 'correctanswer1', 'correctanswer2', 'correctanswer3', 'correctanswer4', 'correctanswer5', 'eqpoints1' , 'eqpoints2' ,'eqpoints3' ,'eqpoints4' ,'eqpoints5' ]


class StudentAnswerForm(ModelForm):
    studentanswer1 = forms.CharField(widget=forms.TextInput())
    studentanswer2 = forms.CharField(widget=forms.TextInput())
    studentanswer3 = forms.CharField(widget=forms.TextInput())
    studentanswer4 = forms.CharField(widget=forms.TextInput())
    studentanswer5 = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = StudentAnswer
        fields = ['studentanswer1', 'studentanswer2', 'studentanswer3','studentanswer4', 'studentanswer5']


class QuizResultForm(ModelForm):
    quiz_id = forms.IntegerField(widget=forms.TextInput())

    class Meta:
        model = QuizResult
        fields = ['quiz_id']