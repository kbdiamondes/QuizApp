from django.contrib import messages
from django.db import connection
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.contrib.auth import logout as auth_logout

from .forms import CreateQuizForm, StudentAnswerForm, QuizResultForm, QuizBankForm, StudentRegistration, \
    TeacherRegistration
from .models import Quiz, User, Teacher, Student, StudentAnswer


# Create your views here.

class HomeView(View):
    template = 'menu.html'

    def get(self, request):
        return render(request, self.template)

class RegisterStudent(View):
    template = 'student-registration.html'

    def get(self, request):
        form = StudentRegistration()
        return render(request, self.template, {'form': form})

    def post(self,request):
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template, {'form': form})


class RegisterTeacher(View):
    template = 'teacher-registration.html'

    def get(self, request):
        form = TeacherRegistration()
        return render(request, self.template, {'form': form})

    def post(self,request):
        form = TeacherRegistration(request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template, {'form': form})



class Login(View):
    template = 'login.html'

    def get(self, request):
        request.session['visits'] = int(request.session.get('visits', 0)) + 1
        return render(request, self.template)

    def post(self, request):
        uname = request.POST['username']
        pwd = request.POST['password']

        try:
            user = User.objects.get(pk=uname)
            if user.password == pwd:
                request.session['username'] = user.username
                request.session['type'] = user.type
                return redirect(reverse('createQuiz:main_menu'))
        except User.DoesNotExist:
            user = None

        return render(request, self.template, {'msg':'Incorrect username/password.'})


class CreateQuiz(View):
    template = 'addQuiz.html'

    def get(self, request):
        form = CreateQuizForm()
        request.session['visits'] = int(request.session.get('visits', 0)) + 1
        return render(request, self.template, {'form':form})

    def logout(self,request):
        auth_logout(request)
        return render(request, self.template)

    def post(self, request):
        form = CreateQuizForm(request.POST)
        if form.is_valid():
            quiz = form.save()
            teacher = Teacher.objects.get(pk=request.session['username'])
            quiz.teacher.add(teacher)
        return render(request, self.template, {'form':form})


class AnswerQuiz(View):
    template = 'ansQuiz.html'


    def get(self, request):
        form = StudentAnswerForm()
        request.session['visits'] = int(request.session.get('visits', 0)) + 1
        quiz = Quiz.objects.all() #get data from all objects on Quiz model
        return render(request, self.template,{'quiz':quiz, 'form':form})

    def post(self,request):
        form = StudentAnswerForm(request.POST)
        quiz = Quiz.objects.all()
        if form.is_valid():
            answer = form.save()
            student = Student.objects.get(pk=request.session['username'])
            answer.student.add(student)

        return render(request, self.template, {'quiz':quiz,'form':form})


class QuizResult(View):
    template = 'quizResult.html'

    def get(self,request):
        cursor = connection.cursor()
        cursor.callproc('QuizEvent.displayTakenQuizByStudent', [request.session['username']])
        studAns = cursor.fetchall()

        return render(request, self.template,{'quiz':studAns})

class QuizBank(View):
    template = "quizBank.html"

    def get(self, request):
        form = QuizBankForm
        cursor = connection.cursor()
        cursor.callproc('QuizEvent.displayQuizBank')
        displayRecords = cursor.fetchall()
        return render(request, self.template, {'displayRecords':displayRecords ,'form':form})

    def post(self, request):
        #form = QuizBankForm(request.POST)
        #quizid = Quiz.objects.get(pk=request.POST['quizid'])
        form = QuizBankForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template, {'form':form})


class LogOut(View):
    template = 'logout.html'

    def get(self, request):
        auth_logout(request)
        return render(request, self.template)



class CloseQuiz(View):
    template = 'closeQuiz.html'

    def get(self, request):
        auth_logout(request)
        return render(request, self.template)


class EditQuestion(View):
    template = 'EditQuestion.html'

    def get(self, request):
        form = CreateQuizForm()
        quiz = Quiz.objects.all()
        return render(request, self.template,{'quiz':quiz, 'form':form})

    def editquiz(request,questionid):
        displayquiz=Quiz.objects.get(questionid=questionid)
        return render(request,"edit.html",{"Quiz":displayquiz})

    def delete(request, questionid):
        quiz = Quiz.objects.filter(questionid=questionid)
        quiz.delete()
        quiz = Quiz.objects.all()
        return render(request,"EditQuestion.html", {'quiz':quiz})

    def updatequiz(request,questionid):
        updatequiz=Quiz.objects.get(questionid=questionid)
        form=CreateQuizForm(request.POST, instance=updatequiz)
        if form.is_valid():
            form.save()
            messages.success(request,"Question Update Successfully...!")
            return render(request,"edit.html",{"Quiz":updatequiz})
