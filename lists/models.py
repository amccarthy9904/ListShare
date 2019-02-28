from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    PRIVACY_CHOICES = [('0', 'Private'), ('1', 'Public')]
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField()
    editors = models.ManyToManyField('Profile', related_name='editors', blank='True')
    owner = models.ForeignKey('Profile', models.SET_NULL, null=True, related_name='owner', blank='True')
    private = models.CharField(choices=PRIVACY_CHOICES, max_length=1)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    owns = models.ManyToManyField('List', related_name='owner_of')
    edits = models.ManyToManyField('List', related_name='editor_of')
    def __str__(self):
        return self.user.username
