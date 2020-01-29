from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.channel.views import ChannelView

router = DefaultRouter()
router.register(r'', ChannelView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include('apps.post.urls')),
    path('api/channels/', include(router.urls)),
    path('api/auth/', include('apps.user.urls')),
    path('api/home/', include('apps.home.urls')),
    path('', include('rest_framework.urls')),
    # path('api/channel/', include('apps.channel.urls')),
    # path('notification/', include('apps.notification.urls'))
]
