from .models import Board
from rest_framework import serializers

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id','title', 'archive', 'date_created', 'date_modified', 'owner')

