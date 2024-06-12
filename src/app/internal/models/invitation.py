from django.db import models
from django.utils import timezone

from app.internal.models.family import Family


class Invitation(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        time = self.created.strftime('%d.%m.%Y %H:%M %Z')
        return f"{self.family} ({time})"

    def update_created(self):
        self.created = timezone.now()
        self.save()