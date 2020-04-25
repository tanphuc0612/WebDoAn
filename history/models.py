from django.db import models
from user.models import Profile
from exam.models import Exam

class History(models.Model):
    time_exam = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        unique_together = (('time_exam','user_id', 'exam_id'),)
    
    def __str__(self):
        return f'{self.user_id} + {self.time_exam}'
