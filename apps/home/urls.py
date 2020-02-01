from django.urls import path
from apps.home import views

urlpatterns = [
    path('liked', views.LikedList.as_view()),
    path('latest', views.LatestList.as_view()),
    path('subscriptions', views.SubscriptionsList.as_view()),
    path('trending', views.TrendingList.as_view()),
]