from django import forms
from app.internal.forms.placeholder import PlaceholderForm


class LogInForm(PlaceholderForm):
    username = forms.CharField(max_length=32, help_text='Username')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(), help_text='Password')
