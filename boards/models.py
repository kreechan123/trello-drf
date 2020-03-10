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
    archive = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


def uploadto(instance, filename):
    return '/'.join(['uploads', instance.board.board.title, filename])
class Card(models.Model):
    """ Card Model
    """
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=200, blank=True, null=True)
    image = models.FileField(upload_to=uploadto, blank=True, null=True)
    card_image_name = models.CharField(max_length=128, blank=True, null=True)
    boardlist = models.ForeignKey(Boardlist, on_delete=models.CASCADE, null=False)
    position = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def get_image_name(self):
        return self.image.name

class BoardMember(models.Model):
    """BoardMember Model
    """
    board = models.ForeignKey(Board,on_delete=models.CASCADE)
    archive = models.BooleanField(default=False)
    member = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank="True")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class CardComment(models.Model):
    """CardComment Model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank="True")
    comment = models.TextField(max_length=200, blank=True, null=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE,null=True, blank="True")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)