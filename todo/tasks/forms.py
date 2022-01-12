from django import forms
from django.forms import ModelForm

from .models import *

# Create the model class form

class TaskForm(forms.ModelForm):
    # Define which model this form is linked to and which fields are included
    class Meta:
        model = Task
        fields = '__all__'