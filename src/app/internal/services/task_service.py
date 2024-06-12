from typing import Any
from app.internal.models.app_user import AppUser
from app.internal.models.task import Task
from app.internal.models.task_role import TaskRole
from app.internal.models.family import Family
from app.internal.models.family_role import FamilyRole
from datetime import datetime, timedelta
from django.db.models import Q
from app.internal.services.notification_service import *


def create_task(app_user, family_id, name, tag, description, start_time, end_time, status, private):
    task = Task.objects.create(
        family=Family.objects.get(id=family_id),
        name=name,
        tag=tag,
        description=description,
        start_time=start_time,
        end_time=end_time,
        status=status,
        private=private,
    )
    TaskRole.objects.create(
        app_user=app_user,
        task=task,
        role='Owner'
    )
    users = FamilyRole.objects.filter(family__id=family_id).all().values_list('app_user', flat=True)
    create_notifications(users, new_task_message(app_user, task), 'Task')

def update_task(app_user, task_id, family_id, name, tag, description, start_time, end_time, status, private):
    Task.objects.filter(id=task_id).update(
        family=Family.objects.get(id=family_id),
        name=name,
        tag=tag,
        description=description,
        start_time=start_time,
        end_time=end_time,
        status=status,
        private=private,
    )
    if private == 'Личное':
        return
    task = Task.objects.get(id=task_id)
        
    if private == 'Для этой семьи':
        users = FamilyRole.objects.filter(family__id=family_id).values_list('app_user', flat=True)
        create_notifications(users, update_task_message(app_user, task), 'Task')
    else:
        families = FamilyRole.objects.filter(app_user=app_user).values_list('family', flat=True)
        users = FamilyRole.objects.filter(family__in=families).values_list('app_user', flat=True)
        create_notifications(users, update_task_message(app_user, task), 'Task')

def get_day_task_list(user, date=None):
    if date is None:
        return TaskRole.objects.filter(app_user=user).values_list('task', flat=True)
    else:
        current_date = date
        start_of_day = datetime.combine(current_date, datetime.min.time())
        end_of_day = datetime.combine(current_date, datetime.max.time())
        user = AppUser.objects.filter(username=user).first()
        families = FamilyRole.objects.filter(app_user=user).values_list('family', flat=True)
        users = FamilyRole.objects.filter(family__in=families).values_list('app_user', flat=True)
        return TaskRole.objects.filter(
            Q(task__start_time__gte=start_of_day) & Q(task__start_time__lte=end_of_day)
            & Q(app_user__in=users)
            & ~Q(task__status='Не выполнена') & ~Q(task__status='Завершена')
            & (
                (Q(app_user=user))
                | (Q(task__private='Личное') & Q(app_user=user))
                | (Q(task__private='Для этой семьи') & Q(task__family__in=families))
                | (Q(task__private='Для всех') & Q(app_user__in=users))
            )
        ).all()

        
    