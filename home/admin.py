from django.contrib import admin
from .models import Post, Comment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('user', 'slug', 'updated_at')
    search_fields=('slug', 'body')
    list_filter=('updated_at',)
    prepopulated_fields={'slug':('body',)}
    raw_id_fields=('user',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('user', 'post', 'created_at', 'is_reply')
    raw_id_fields=('user', 'post', 'reply')