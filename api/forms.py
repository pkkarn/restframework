from django.forms import ModelForm
from .models import *


class QueryForm(ModelForm):
    picture = models.ImageField(upload_to='pictures/', default='pctures/None/no-img.jpg')
    class Meta:
        model = Query
        fields = ['title', 'question_type', 'description', 'picture']
