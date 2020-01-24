from django.urls import path
from apps.user import views

urlpatterns = [
    path('', views.ProfileList.as_view()),
    path('<str:username>', views.ProfileDetail.as_view())
]