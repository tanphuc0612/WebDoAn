from django.contrib import admin
from .models import Answer, Question, Quiz, StudentAnswer, TakenQuiz

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(StudentAnswer)
admin.site.register(TakenQuiz)


