from django.urls import path
from apps.post import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>', views.PostDetail.as_view()),
    path('<int:pk>/like', views.LikePost.as_view()),
    path('<int:post_id>/comments', views.CommentList.as_view()),
    path('<int:post_id>/comments/<int:id>/', views.CommentDetail.as_view()),
    path('<int:post_id>/comments/<int:id>/like',
         views.CommentDetail.as_view()),
    path('<int:post_id>/comments/<int:id>/dislike',
         views.CommentDetail.as_view()),
]