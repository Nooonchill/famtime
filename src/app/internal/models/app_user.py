from django.db import models


class AppUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
