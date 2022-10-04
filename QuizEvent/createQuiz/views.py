from django.shortcuts import render
from django.views import View

from .forms import CreateQuizForm, StudentAnswerForm, QuizResultForm


# Create your views here.


class CreateQuiz(View):
    template = 'createQuiz.html'

    def get(self, request):
        form = CreateQuizForm()
        return render(request, self.template, {'form':form})


class AnswerQuiz(View):
    template = 'ansQuiz.html'

    def get(self, request):
        form = StudentAnswerForm()
        return render(request, self.template, {'form':form})


class QuizResult(View):
    template = 'quizResult.html'

    def get(self,request):
        form = QuizResultForm
        return render(request, self.template,{'form':form})
