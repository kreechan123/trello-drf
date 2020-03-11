from .models import Board, Boardlist, Card, BoardMember, CardComment
from rest_framework import serializers


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id','title', 'archive', 'date_created', 'date_modified', 'owner')
        read_only_fields = ['owner']


class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boardlist
        fields = ('id','title', 'archive', 'date_created', 'date_modified','board')


class BoardCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id','title', 'description', 'image', 'card_image_name', 'boardlist', 'position', 'date_created', 'date_modified')
        read_only_fields = ['boardlist']


class CardCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardComment
        fields = ('id','user', 'comment', 'card', 'date_created', 'date_modified')
        read_only_fields = ['user']


class BoardMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardMember
        fields = ('id','board', 'archive', 'member', 'date_created', 'date_modified')
