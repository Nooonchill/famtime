from django.db import models

from app.internal.models.app_user import AppUser
from app.internal.models.family import Family


class Notification(models.Model):
    id = models.BigAutoField(primary_key=True)
    app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.family} - {self.app_user} - {self.created}'
