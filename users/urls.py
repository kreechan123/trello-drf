from django.urls import path
from . import views
from .views import LoginViewSet, RegisterViewSet


urlpatterns = [
    path('', LoginViewSet.as_view({'post':'login'})),
    path('register/', RegisterViewSet.as_view({'post':'register'})),

]