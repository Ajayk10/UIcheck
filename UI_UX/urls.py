from django.urls import path
from UI_UX import views

urlpatterns = [
    path('', views.index.as_view(), name = 'index'),
    path('content/', views.content, name = 'content'),
    path('profile/', views.profile, name = 'profile'),
    path('purchase/', views.purchase, name = 'purchase'),
    ]
