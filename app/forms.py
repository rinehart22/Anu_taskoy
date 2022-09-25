from . models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib import messages

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
    # def clean(self):
    #     stud = self.cleaned_data['name'].lower()
    #     sub = self.cleaned_data['subject'].lower()
    #     if Student.objects.filter(name=stud, subject=sub).exists():
          
    #         raise forms.ValidationError('record already exists')
    #     return stud


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']