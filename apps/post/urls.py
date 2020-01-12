from django.urls import path
from apps.post import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>', views.PostDetail.as_view()),
    path('<int:post_id>/comments', views.CommentList.as_view()),
    path('<int:post_id>/comments/<int:id>/', views.CommentDetail.as_view()),
]