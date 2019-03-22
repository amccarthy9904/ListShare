from django.forms import ModelForm
from .models import List

class EditListForm(ModelForm):
    class Meta:
        model = List
        #fields = ['name', 'content', 'editors', 'viewers', 'private', 'type']
        fields = ['content']
