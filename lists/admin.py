from django.contrib import admin
from .models import List
from .models import User

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'private']
    #Profile.list_display = []
    pass
