from django.db import models
from colorfield.fields import ColorField


class Family(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    color = ColorField(default='#FFFFFF')

    def __str__(self):
        return f"{self.name} #{self.id}"