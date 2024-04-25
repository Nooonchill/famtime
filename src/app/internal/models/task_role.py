from django.db import models

from app.internal.models.app_user import AppUser
from app.internal.models.task import Task


class TaskRole(models.Model):
    TASK_ROLE_CHOICE = [
        ('Owner', 'Owner'),
        ('Editor', 'Editor'),
        ('Executor', 'Executor'),
    ]
    app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    role = models.CharField(max_length=8, choices=TASK_ROLE_CHOICE)

    def __str__(self):
        return f'{self.app_user} - {self.task}'
