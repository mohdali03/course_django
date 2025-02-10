from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


CustomStudent = get_user_model()

class StudentForm(UserCreationForm):
    class Meta:
        model = CustomStudent
        fields = ('username', 'email', 'password1', 'password2')