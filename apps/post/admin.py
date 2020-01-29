from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'owner', 'channel', 'date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'post', 'owner', 'date')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
