from django import forms
from .models import List

class NewListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name', 'content', 'editors', 'private']

class EditorEditListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['content']

class OwnerEditListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name', 'content', 'owner', 'editors', 'private']
