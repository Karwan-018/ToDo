from django import forms
from .models import ToDoItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['title', 'description', 'completed']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']