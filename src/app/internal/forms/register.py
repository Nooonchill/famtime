from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=32)
    email = forms.EmailField()
    password = forms.CharField(max_length=128)
    repeat_password = forms.CharField(max_length=128)
