from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    """Board Model
    """
    title = models.CharField(max_length=200)
    archive = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Boardlist(models.Model):
    """Boardlist Model
    """
    title = models.CharField(max_length=200)    
    archived = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title