from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include('apps.post.urls')),
    path('api/auth/', include('apps.user.urls')),
    path('api/home/', include('apps.home.urls')),
    # path('notification/', include('apps.notification.urls'))
    path('api/channels/', include('apps.channel.urls')),
    path('', include('rest_framework.urls')),
]
