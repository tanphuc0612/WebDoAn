from django.forms import ModelForm
from .models import Questions

class QuestionsForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['question','answer_a','answer_b','answer_c','answer_d', 'result']