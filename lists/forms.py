from django import forms
from .models import List

class EditListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name', 'content', 'editors', 'viewers', 'private', 'type']
