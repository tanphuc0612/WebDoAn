from django.db import models
from users.models import (Grade, Student)

class Quiz(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='quizzes')
    name  = models.CharField(max_length=255)
    grade = models.ForeignKey('users.Grade', on_delete=models.CASCADE,related_name='quizzes')
    
    def __str__(self):
        return self.name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField('Question')

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text     = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)
    
    def __str__(self):
        return self.text



class TakenQuiz(models.Model):
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE, related_name='taken_quizzes')
    quiz    = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_quizzes')
    score   = models.IntegerField(default=0)
    percentage = models.FloatField()
    date    = models.DateTimeField(auto_now_add=True)


class StudentAnswer(models.Model):
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE, related_name='quiz_answers')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='+')


    
