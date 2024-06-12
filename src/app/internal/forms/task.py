from django import forms
from app.internal.models.task import Task

class PlaceholderModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlaceholderModelForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.help_text

class CreateTaskForm(PlaceholderModelForm):
    class Meta:
        model = Task
        fields = ['name', 'tag', 'description', 'start_time', 'end_time', 'status', 'private']
        labels = {
            'name': 'Название',
            'tag': 'Тег',
            'description': 'Описание',
            'start_time': 'Начало',
            'end_time': 'Конец',
            'status': 'Статус',
            'private': 'Доступ'
        }
        help_texts = {
            'name': 'Название',
            'tag': 'Тег',
            'description': 'Описание',
            'start_time': 'Начало',
            'end_time': 'Конец',
            'status': 'Статус',
            'private': 'Доступ'
        }
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

class UpdateTaskForm(PlaceholderModelForm):
    class Meta:
        model = Task
        fields = ['name', 'tag', 'description', 'start_time', 'end_time', 'status', 'private']
        labels = {
            'name': 'Название',
            'tag': 'Тег',
            'description': 'Описание',
            'start_time': 'Начало',
            'end_time': 'Конец',
            'status': 'Статус',
            'private': 'Доступ'
        }
        help_texts = {
            'name': 'Название',
            'tag': 'Тег',
            'description': 'Описание',
            'start_time': 'Начало',
            'end_time': 'Конец',
            'status': 'Статус',
            'private': 'Доступ'
        }
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }