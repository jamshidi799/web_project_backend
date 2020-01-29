from django.urls import path

from apps import post
from apps.home import views

urlpatterns = [
    path('', post.views.PostList.as_view()),
    path('trending/', views.TrendPosts.as_view()),
    path('followed/', views.FollowedPosts.as_view()),
    path('latest/', views.LatestPosts.as_view()),
    path('subscriptions/', views.SubPosts.as_view()),
]