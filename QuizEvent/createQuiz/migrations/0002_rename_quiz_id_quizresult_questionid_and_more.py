# Generated by Django 4.1.2 on 2022-10-18 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('createQuiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizresult',
            old_name='quiz_id',
            new_name='questionid',
        ),
        migrations.RemoveField(
            model_name='quizresult',
            name='nickname',
        ),
    ]
