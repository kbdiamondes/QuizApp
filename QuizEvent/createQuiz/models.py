from django.db import models


# Create your models here.


class User(models.Model):
    type_user = (('S', 'Student'), ('T', 'Teacher'))
    username = models.CharField(max_length=15, null=False, primary_key=True)
    password = models.CharField(max_length=10, null=False)
    firstname = models.CharField(max_length=50, null=False)
    middlename = models.CharField(max_length=50, null=False)
    lastname = models.CharField(max_length=50, null=False)
    type = models.CharField(max_length=1, choices=type_user)


class Student(User):
    nickname = models.CharField(max_length=15)
    course = models.CharField(max_length=50)



class Teacher(User):
    degree = models.CharField(max_length=50)


class Quiz(models.Model):
    quizid = models.AutoField(primary_key=True)
    subjectname = models.CharField(max_length=50)
    username = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    question1 = models.CharField(max_length=50)
    question2 = models.CharField(max_length=50)
    question3 = models.CharField(max_length=50)
    question4 = models.CharField(max_length=50)
    question5 = models.CharField(max_length=50)
    correctanswer1 = models.CharField(max_length=50)
    correctanswer2 = models.CharField(max_length=50)
    correctanswer3 = models.CharField(max_length=50)
    correctanswer4 = models.CharField(max_length=50)
    correctanswer5 = models.CharField(max_length=50)
    eqpoints1 = models.CharField(max_length=50)
    eqpoints2 = models.CharField(max_length=50)
    eqpoints3 = models.CharField(max_length=50)
    eqpoints4 = models.CharField(max_length=50)
    eqpoints5 = models.CharField(max_length=50)


class StudentAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(Student, on_delete=models.CASCADE)
    quizid = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    studentanswer1 = models.CharField(max_length=50)
    studentanswer2 = models.CharField(max_length=50)
    studentanswer3 = models.CharField(max_length=50)
    studentanswer4 = models.CharField(max_length=50)
    studentanswer5 = models.CharField(max_length=50)



class QuizResult(models.Model):
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    nickname = models.ForeignKey(Student, on_delete=models.CASCADE)
    studentscore = models.IntegerField(default=0, null=False)
    cAns1 = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=False,  related_name="cAns1")





