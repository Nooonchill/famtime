from django.shortcuts import render
from app.internal.services.user_service import *


def auth(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        log_in_form = LogInForm(request.POST)
        if register_form.is_valid():
            try_register_user(register_form)

        if log_in_form.is_valid():
            try_log_in_user(log_in_form)

    else:
        register_form = RegisterForm()
        log_in_form = LogInForm()
    context = {'register_form': register_form, 'log_in_form': log_in_form}
    return render(request, 'auth.html', context)
