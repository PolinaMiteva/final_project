from django.urls import path
from blog.views import AllBlogPosts, one_blog_post, edit_comment, delete_comment

urlpatterns = [
    path('all_posts/', AllBlogPosts.as_view(), name='all-blog-posts'),
    path('all_posts/post-<int:pk>/', one_blog_post, name='one-post'),
    path('all_posts/edit-comment-<int:pk>', edit_comment, name='edit-comment'),
    path('all_post/delete-comment-<int:pk>', delete_comment, name='delete-comment')
]