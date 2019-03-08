from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

def get_user_deleted():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class List(models.Model):
    #PRIVACY_CHOICES = [('0', 'Private'), ('1', 'Public')]
    TYPE_CHOICES = [('0', 'Text'), ('1', 'Itemized')]
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(null=True)
    owner = models.ForeignKey(User, related_name='owner_of', null=True, blank=True, on_delete=models.CASCADE)
    editors = models.ManyToManyField(User, related_name='editor_of', null=True, blank=True)
    viewers = models.ManyToManyField(User, related_name='viewer_of', null=True, blank=True)
    private = models.BooleanField(default=True, null=True, blank=True)
    type = models.BooleanField(choices=TYPE_CHOICES, max_length=1, null=True, blank=True)

    def __str__(self):
        return self.name

class Items(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(null=True)
    creator = models.ForeignKey(User, related_name='creator_of', null=True, blank=True, on_delete=models.SET(get_user_deleted))
    list = models.ForeignKey(List, related_name='items', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
