from django.contrib import admin

from .models import User, Student, Teacher, Quiz, StudentAnswer, QuizResult

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Quiz)
admin.site.register(StudentAnswer)
admin.site.register(QuizResult)