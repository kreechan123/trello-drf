from django.urls import path
from rest_framework import routers
from .views import BoardViewSet
from . import views


urlpatterns = [
    path('boards/', BoardViewSet.as_view({'get': 'board_list','post':'board_create'})),
    path('boards/<int:id>/', BoardViewSet.as_view({'get': 'board_detail', 'post': 'board_delete'})),
]