# Generated by Django 4.1.2 on 2022-10-13 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('questionid', models.IntegerField(unique=True)),
                ('quizid', models.AutoField(primary_key=True, serialize=False)),
                ('subjectname', models.CharField(max_length=50)),
                ('question', models.CharField(max_length=50)),
                ('correctanswer', models.CharField(max_length=50)),
                ('eqpoints', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=10)),
                ('firstname', models.CharField(max_length=50)),
                ('middlename', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('S', 'Student'), ('T', 'Teacher')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='createQuiz.user')),
                ('course', models.CharField(max_length=50)),
            ],
            bases=('createQuiz.user',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='createQuiz.user')),
                ('degree', models.CharField(max_length=50)),
            ],
            bases=('createQuiz.user',),
        ),
        migrations.CreateModel(
            name='QuizBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionid', models.IntegerField()),
                ('quizid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='createQuiz.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('quizid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='quiz_id', serialize=False, to='createQuiz.quiz')),
                ('studentanswer', models.CharField(max_length=50)),
                ('questionid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_question', to='createQuiz.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentscore', models.IntegerField(default=0)),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='createQuiz.quiz')),
                ('nickname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='createQuiz.student')),
            ],
        ),
    ]
