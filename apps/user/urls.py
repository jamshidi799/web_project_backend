from django.urls import path
from apps.user import views

urlpatterns = [
    path('small', views.ProfileSmallList.as_view()),
    path('<slug:username>', views.ProfileView.as_view())
]