from django.contrib import admin
from .models import Profile, Connection


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )


class ConnectionAdmin(admin.ModelAdmin):
    list_display = (
        'following',
        'creator',
    )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Connection, ConnectionAdmin)
