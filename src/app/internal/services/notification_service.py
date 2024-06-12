from app.internal.models.notification import Notification
from app.internal.models.app_user import AppUser


def create_notifications(users, message, tag):
    users = AppUser.objects.filter(id__in=users)
    for user in users:
        create_notification(user, message, tag)

def create_notification(app_user, message, tag):
    notification = Notification.objects.create(
        app_user=app_user,
        message=message,
        tag=tag,
    )
    return notification

def new_task_message(app_user, task):
    return f'{app_user.username} добавил новую задачу: "{task.name}"'

def update_task_message(app_user, task):
    return f'{app_user.username} обновил задачу: "{task.name}"'

def new_user_message(app_user, family):
    return f'Новый пользователь добавлен в семью "{family}": "{app_user.username}"'

def add_family_message(family):
    return f'Добавлена новая семья: "{family.name}"'

def new_family_message(family):
    return f'Создана новая семья: "{family.name}"'

def get_user_notifications(app_user):
    return Notification.objects.filter(app_user=app_user).order_by('-created')