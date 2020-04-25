from django.db import models

class Question(models.Model):

    question = models.CharField(default='empty', max_length=200)

    descipt_A = models.TextField(default='question a')
    descipt_B = models.TextField(default='question b')
    descipt_C = models.TextField(default='question c')
    descipt_D = models.TextField(default='question d')
    
    ANSWER_CHOICES = (
        ('A', 'answer a'),
        ('B', 'answer b'),
        ('C', 'answer c'),
        ('D', 'answer d')
    )
    answer = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='A')

    def __str__(self):
        return f'{self.question}'



class Exam(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    exam_id = models.AutoField(primary_key=True)

    class Meta:
        unique_together = (('question_id', 'exam_id'),)
    
    def __str__(self):
        return f'question_id: {self.question_id} + exam_id: {self.exam_id}'