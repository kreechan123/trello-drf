from .models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(max_length=200)
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')