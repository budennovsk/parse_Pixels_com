from django import forms
from .models import *
class FileForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'