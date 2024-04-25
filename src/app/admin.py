from django.contrib import admin

from app.internal.models.app_user import AppUser
from app.internal.models.family import Family
from app.internal.models.role import Role
from app.internal.models.invitation import Invitation

admin.site.site_title = "famtime"
admin.site.site_header = "famtime"

admin.site.register(AppUser)
admin.site.register(Family)
admin.site.register(Role)
admin.site.register(Invitation)