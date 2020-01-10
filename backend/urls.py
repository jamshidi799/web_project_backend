from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/post', include('apps.post.urls')),
    path('api/user', include('apps.user.urls')),
    path('api/channel', include('apps.channel.urls')),
    path('notification', include('apps.notification.urls'))
]
