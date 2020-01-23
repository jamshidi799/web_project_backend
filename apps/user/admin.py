from django.contrib import admin
from .models import Profile, Follower


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Follower)
