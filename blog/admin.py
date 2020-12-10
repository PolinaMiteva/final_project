from django.contrib import admin
from blog.models import Comment, Post

# admin.site.register(Comment)
# admin.site.register(Post)


@admin.register(Post)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = 'id',
    list_display = ('id', 'author', 'title', 'body', 'post_datetime', 'header_img')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = 'id',
    list_display = ('id', 'user', 'body', 'comment_datetime')
