from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class AppUser(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    registered = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
