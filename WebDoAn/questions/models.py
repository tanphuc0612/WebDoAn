from django.db import models

class Questions(models.Model):

    question = models.TextField(default='content of question')

    answer_a = models.TextField(default='answer A for questions ')
    answer_b = models.TextField(default='answer B for questions ')
    answer_c = models.TextField(default='answer C for questions ')
    answer_d = models.TextField(default='answer D for questions ')

    ANSWER_CHOICES = [
        ('a', 'answer is a'),
        ('b', 'answer is b'),
        ('c', 'answer is c'),
        ('d', 'answer is d'),
    ]

    result = models.CharField(max_length=1, default='a', choices=ANSWER_CHOICES)

    def __str__(self):
        return f'{self.id} : {self.result}'
    
