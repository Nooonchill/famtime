from django import forms
from colorfield.widgets import ColorWidget
from app.internal.models.family import Family

class PlaceholderModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlaceholderModelForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['placeholder'] = 'Family Name'


class CreateFamilyForm(PlaceholderModelForm):
    class Meta:
        model = Family
        fields = ['name', 'color']
        help_textes = {
            'name': ('Family Name'),
            'color': ('Family Color'),
        }