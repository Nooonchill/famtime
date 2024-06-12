from typing import Any
from sqlite3 import IntegrityError

from app.internal.models.app_user import AppUser
from app.internal.forms.register import RegisterForm
from app.internal.forms.log_in import LogInForm
from django.core.exceptions import ValidationError


def try_get_user_by_param(parameter: str, value: Any) -> AppUser | None:
    try:
        user = AppUser.objects.get(**{parameter: value})
    except:
        user = None
    return user


def try_register_user(register_form: RegisterForm) -> AppUser | None:
    username = register_form.cleaned_data['username']
    password = register_form.cleaned_data['password']
    email = register_form.cleaned_data['email']
    if register_form.cleaned_data['password'] == register_form.cleaned_data['repeat_password']:
        try:
            user = AppUser.objects.create(
                username=username,
                email=email,
                password=password,
                first_name=register_form.cleaned_data['first_name'],
                last_name=register_form.cleaned_data['last_name'],
            )
        except:
            user = None
    else:
        raise ValidationError("repeat password error")

    return user


def try_log_in_user(log_in_form: LogInForm) -> AppUser | None:
    username = log_in_form.cleaned_data['username']
    user = try_get_user_by_param('username', username)
    if user is None:
        raise ValidationError("user not found")
    elif user.password != log_in_form.cleaned_data['password']:
        raise ValidationError("password error")
    return user
