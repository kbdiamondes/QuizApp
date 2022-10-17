from django.forms import ModelForm
from django import forms
from .models import Quiz, StudentAnswer, QuizResult, Student, User, Teacher


class StudentRegistration(ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput)
    firstname = forms.CharField(widget=forms.TextInput())
    middlename = forms.CharField(widget=forms.TextInput())
    lastname = forms.CharField(widget=forms.TextInput())
    type = 'S'
    course = forms.CharField(widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super(StudentRegistration, self).__init__(*args, **kwargs)
        self.instance.type = self.type
        self.fields['middlename'].required = False
    class Meta:
        model = Student
        fields = ['username', 'password', 'firstname', 'middlename', 'lastname', 'course']


class TeacherRegistration(ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput)
    firstname = forms.CharField(widget=forms.TextInput())
    middlename = forms.CharField(widget=forms.TextInput())
    lastname = forms.CharField(widget=forms.TextInput())
    type = 'T'
    degree = forms.CharField(widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super(TeacherRegistration, self).__init__(*args, **kwargs)
        self.instance.type = self.type
        self.fields['middlename'].required = False
    class Meta:
        model = Teacher
        fields = ['username', 'password', 'firstname', 'middlename', 'lastname', 'degree']


class CreateQuizForm(ModelForm):
    subjectname = forms.CharField(widget=forms.TextInput())
    question = forms.CharField(widget=forms.TextInput())
    questionid = forms.IntegerField(widget=forms.NumberInput())
    correctanswer = forms.CharField(widget=forms.TextInput())
    eqpoints = forms.IntegerField(widget=forms.NumberInput())


    class Meta:
        model = Quiz
        fields = ['subjectname', 'questionid','question',  'correctanswer', 'eqpoints']


class StudentAnswerForm(ModelForm):
    questionid = forms.ModelChoiceField(widget=forms.Select(), queryset=Quiz.objects.only('questionid'))
    studentanswer = forms.CharField(widget=forms.TextInput())


    class Meta:
        model = StudentAnswer
        fields = ['questionid','studentanswer']


class QuizResultForm(ModelForm):
    quiz_id = forms.ModelChoiceField(widget=forms.Select(), queryset=Quiz.objects.only('quizid'))

    class Meta:
        model = QuizResult
        fields = ['quiz_id']


class QuizBankForm(ModelForm):
    #quizid = forms.IntegerField(widget=forms.TextInput())
    quizid = forms.ModelChoiceField(widget=forms.Select(), queryset=Quiz.objects.only('quizid'))
    #subjectname = forms.ModelChoiceField(widget=forms.Select(), queryset=Quiz.objects.only())
    questionid = forms.IntegerField(widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super(QuizBankForm, self).__init__(*args, *kwargs)
    class Meta:
        model = Quiz
        fields = ['quizid','questionid']


