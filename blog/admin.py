from django.contrib import admin
from blog.models import Comment, Post


class CommentInlineAdmin(admin.StackedInline):
    model = Comment
    list_display = ('id', 'user', 'body', 'comment_datetime')
    readonly_fields = 'id',


class PostAdmin(admin.ModelAdmin):
    readonly_fields = 'id',
    list_display = ('id', 'author', 'title', 'body', 'post_datetime', 'header_img')

    inlines = (
        CommentInlineAdmin,
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
