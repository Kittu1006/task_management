from django import forms
from django.forms import fields
from .models import TaskDb

class TaskForms(forms.ModelForm):
    class Meta:
        model = TaskDb
        fields = ['task','priority']
