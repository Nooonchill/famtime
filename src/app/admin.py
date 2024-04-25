from django.contrib import admin

from app.internal.models.app_user import AppUser

admin.site.site_title = "famtime"
admin.site.site_header = "famtime"

admin.site.register(AppUser)