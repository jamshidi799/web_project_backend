from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static  # new
from django.conf import settings  # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include('apps.post.urls')),
    path('api/channels/', include('apps.channel.urls')),
    path('api/auth/', include('apps.user.urls')),
    path('', include('rest_framework.urls')),
    path('api/feed/', include('apps.home.urls')),
    path('api/notification/', include('apps.notification.urls')),
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
