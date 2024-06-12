from django import forms
from app.internal.models.invitation import Invitation
from app.internal.forms.placeholder import PlaceholderForm

class AddFamilyForm(PlaceholderForm):
    code = forms.CharField(max_length=6, help_text='Invitation code')