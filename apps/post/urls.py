from django.urls import path
from apps.post import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>', views.PostDetail.as_view()),
    path('<int:pk>/like/<int:user_id>', views.LikePost.as_view()),
    path('<int:post_id>/comments', views.CommentList.as_view()),
    path('<int:post_id>/comments/<int:comment_id>',
         views.CommentDetail.as_view()),
    path('comments/<int:comment_id>/like/<int:user_id>',
         views.CommentLikeView.as_view()),
    path('comments/<int:comment_id>/dislike/<int:user_id>',
         views.CommentDislikeView.as_view()),
]