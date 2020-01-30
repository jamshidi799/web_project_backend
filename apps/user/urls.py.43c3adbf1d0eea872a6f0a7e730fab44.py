from django.urls import path, include
from apps.user import views
from knox import views as knox_views

urlpatterns = [
    path('', include('knox.urls')),
    path('register', views.RegisterAPI.as_view()),
    path('login', views.LoginAPI.as_view()),
    path('user', views.UserAPI.as_view()),
    path('logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('profile', views.ProfileList.as_view()),
    path('profile/<str:username>', views.ProfileDetail.as_view()),
    path('connection', views.ConnectionList.as_view()),
    path('connection/<int:creator>/<int:following>', views.ConnectionDetail.as_view()),
]