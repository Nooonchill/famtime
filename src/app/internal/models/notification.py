from django.db import models

from app.internal.models.app_user import AppUser
from app.internal.models.family import Family


class Notification(models.Model):
    NOTIFICATION_TAG = [
        ('Task', 'Task'),
        ('Memeber', 'Member'),
        ('Family', 'Family'),
    ]
    id = models.BigAutoField(primary_key=True)
    app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    message = models.TextField()
    tag = models.CharField(max_length=12, choices=NOTIFICATION_TAG)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.app_user} - {self.created}'
