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

    def __str__(self):
        return self.username + ' ' + self.firstname + ' ' + self.lastname + ' ' + self.type


class Student(User):
    course = models.CharField(max_length=50, null=False)



class Teacher(User):
    degree = models.CharField(max_length=50, null=False)


class Quiz(models.Model):
    quizid = models.AutoField(primary_key=True)
    subjectname = models.CharField(max_length=50)
    question = models.CharField(max_length=50)
    correctanswer = models.CharField(max_length=50)
    eqpoints = models.CharField(max_length=50)

    def __str__(self):
        return str(self.quizid) + ' ' + self.subjectname


class QuizBank(models.Model):
    quizid= models.ForeignKey(Quiz, on_delete=models.CASCADE, primary_key=True)


class StudentAnswer(models.Model):
    username = models.ForeignKey(Student, on_delete=models.CASCADE, primary_key=True)
    quizid = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    studentanswer = models.CharField(max_length=50)


class QuizResult(models.Model):
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    nickname = models.ForeignKey(Student, on_delete=models.CASCADE)
    studentscore = models.IntegerField(default=0, null=False)





