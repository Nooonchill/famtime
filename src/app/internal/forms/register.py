from django import forms
from app.internal.forms.placeholder import PlaceholderForm


class RegisterForm(PlaceholderForm):
    username = forms.CharField(max_length=32, help_text='Username')
    email = forms.EmailField(help_text='Email')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(), help_text='Password')
    repeat_password = forms.CharField(max_length=128, widget=forms.PasswordInput(), help_text='Repeat password')
    first_name = forms.CharField(max_length=64, help_text='First name')
    last_name = forms.CharField(max_length=64, help_text='Last name')
