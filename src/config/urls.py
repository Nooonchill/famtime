from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('auth/', views.auth, name='auth'),
    path('schedule/', views.schedule, name='schedule'),
    path('schedule/tasks/<str:date>/', views.get_tasks_for_date, name='get_tasks_for_date'),
    path('schedule/tags/<str:date>/', views.get_day_tags, name='get_day_tags'),
    path('get-invitation/', views.get_invitation, name='get_invitation'),
]
