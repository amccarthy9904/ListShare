from django.contrib import admin
from .models import List
from .models import Profile

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'private']
    #Profile.list_display = []
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
    pass
