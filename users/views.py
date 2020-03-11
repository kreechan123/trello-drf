from rest_framework import viewsets, permissions
from django.shortcuts import render
from users.serializers import RegisterSerializer
from django.contrib.auth import authenticate, login
from .models import User
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, HttpResponse
from rest_framework.authtoken.models import Token
from django.http import JsonResponse


class LoginViewSet(viewsets.ViewSet):
    """Login view
    """

    def login(self, request, **kwargs):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(self.request, username = username, password = password)
        if user is not None:
            token = Token.objects.get_or_create(user=user)
            return JsonResponse({'token':token.key})
        return JsonResponse({"Error": "Invalid"}, status=400)

class RegisterViewSet(viewsets.ViewSet):
    """Register view
    """
    serializer = RegisterSerializer

    def register(self, request, **kwargs):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return JsonResponse({"Error": "Invalid"}, status=400)