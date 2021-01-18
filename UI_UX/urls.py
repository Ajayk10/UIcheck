from django.urls import path
from .views import *
from django.urls import path,include



urlpatterns = [
    path('', HomeView.as_view(),name = "index"),
    path('article/<int:pk>', ArticleDetail.as_view(),name = "article"),
    path('addfeed/', AddFeedView.as_view(),name = "addfeed"),
    path('article/updatefeed/<int:pk>', UpdateFeedView.as_view(), name="updatefeed"),
    path('article/<int:pk>/deletefeed', DeleteFeedView.as_view(), name="deletefeed"),
    path('like/<int:pk>',LikeView,name = 'like_post'),
    ]
