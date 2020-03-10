from django.contrib import admin
from .models import Board, Boardlist, Card, BoardMember, CardComment

admin.site.register(Board)
admin.site.register(Boardlist)
admin.site.register(Card)
admin.site.register(BoardMember)
admin.site.register(CardComment)
