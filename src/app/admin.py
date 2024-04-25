from django.contrib import admin

from app.internal.models.app_user import AppUser
from app.internal.models.family import Family
from app.internal.models.family_role import FamilyRole
from app.internal.models.invitation import Invitation
from app.internal.models.task import Task
from app.internal.models.notification import Notification

admin.site.site_title = "famtime"
admin.site.site_header = "famtime"

admin.site.register(AppUser)
admin.site.register(Family)
admin.site.register(FamilyRole)
admin.site.register(Invitation)
admin.site.register(Task)
admin.site.register(Notification)