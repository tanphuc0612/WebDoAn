from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_Student = models.BooleanField(default=False)
    is_Teacher = models.BooleanField(default=False)

class Grade(models.Model):
    grade = models.IntegerField(default=6)
    def __str__(self):
        return "{0}".format(self.grade)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField('questions.Quiz', through='TakenQuiz')
    grade   = models.OneToOneField(Grade, on_delete=models.CASCADE, related_name='grade')
    
    def get_unanswered_questions(self, quiz):
        answered_questions = self.quiz_answers.filter(answer__question__quiz=quiz).values_list('answer__question__pk', flat=True)
        questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
        return questions
    
    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username