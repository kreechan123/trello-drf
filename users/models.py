from django.db import models
from django.contrib.auth.models import User

def avatar(instance, filename):
    return '/'.join(['avatars', instance.board.board.title, filename])
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.FileField(upload_to=avatar, blank=True, null=True)