from django.db import models

from app.internal.models.family import Family
from app.internal.models.app_user import AppUser


class Role(models.Model):
    USER_ROLE_IN_FAMILY = [
        ('User', 'User'),
        ('Admin', 'Admin'),
        ('Owner', 'Owner'),
    ]
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=5, choices=USER_ROLE_IN_FAMILY)

    class Meta:
        unique_together = (('family', 'app_user'),)

    def __str__(self):
        return f"{self.family} - {self.app_user}"
