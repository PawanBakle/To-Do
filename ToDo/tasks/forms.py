from django.forms import ModelForm
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TaskList
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
class TaskForm(forms.ModelForm):
    class Meta:
        
        model = TaskList
       
        fields = ['title','description','tags']
class EditForm(forms.ModelForm):
    class Meta:
        
        model = TaskList
       
        fields = ('title','description','tags')
class Completed(forms.ModelForm):
    class Meta:
        
        model = TaskList
       
        fields = ('title','description','tags')