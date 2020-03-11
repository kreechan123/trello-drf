from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from boards import views
from users import views


urlpatterns = [
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('boards/', include('boards.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
