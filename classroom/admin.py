from django.contrib import admin

# Register your models here.
from .models import User, Quiz, Question, Answer, Student, TakenQuiz, Grade

admin.site.register(User)
admin.site.register(Grade)
#admin.site.register(Subject)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Student)
admin.site.register(TakenQuiz)