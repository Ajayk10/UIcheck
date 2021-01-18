from django.urls import path
from .views import *
from .models import *
from django.urls import path,include


urlpatterns = [
        path('register/',UserRegisterView.as_view(),name = 'register'),
    ]