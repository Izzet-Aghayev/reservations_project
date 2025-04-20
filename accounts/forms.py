from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'phone_number', 'password1', 'password2')



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
