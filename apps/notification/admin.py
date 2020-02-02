from django.contrib import admin
from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'kind', 'target', 'creator', 'created')


admin.site.register(Notification, NotificationAdmin)