from django.db import models
from django.db.models import BigAutoField

from app.internal.models.family import Family

class Task(models.Model):
    TASK_TAGS = [
        ('E', 'Учеба'),
        ('Работа', 'Работа'),
        ('Дет. сад', 'Детский сад'),
        ('Здоровье', 'Здоровье'),
        ('Уборка', 'Уборка'),
        ('Пища', 'Пища'),
        ('Развлечения', 'Развлечения')
    ]
    TASK_STATUS = [
        ('Ожидает', 'Ожидает'),
        ('Выполняется', 'Выполняется'),
        ('Завершена', 'Завершена'),
        ('Не выполнена', 'Не выполнена')
    ]
    id = BigAutoField(primary_key=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    tag = models.CharField(max_length=11, choices=TASK_TAGS, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=12, choices=TASK_STATUS)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.family} - {self.name}'
