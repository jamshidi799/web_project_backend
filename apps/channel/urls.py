from django.urls import path
from apps.channel import views

urlpatterns = [
    path('', views.ChannelList.as_view()),
    path('<int:pk>/', views.ChannelDetail.as_view()),
    path('<int:pk>/authors/<int:author_id>',
         views.ChannelAuthorsView.as_view()),
]