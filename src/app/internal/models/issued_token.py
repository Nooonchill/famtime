from django.db import models

from app.internal.models.app_user import AppUser


class IssuedToken(models.Model):
    jti = models.CharField(max_length=256, primary_key=True)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    revoked = models.BooleanField(default=False)
    device_id = models.UUIDField(unique=True)

    def __str__(self):
        return f"Токен {self.user}, {self.revoked}"
