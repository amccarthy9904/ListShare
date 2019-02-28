from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    PRIVACY_CHOICES = [('0', 'Private'), ('1', 'Public')]
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(null=True)
    owner = models.ForeignKey(User, related_name='owner_of', null=True, blank=True, on_delete=models.CASCADE)
    editors = models.ManyToManyField(User, related_name='editor_of', null=True, blank=True)
    viewers = models.ManyToManyField(User, related_name='viewer_of', null=True, blank=True)
    private = models.CharField(choices=PRIVACY_CHOICES, max_length=1, null=True, blank=True)

    def __str__(self):
        return self.name
