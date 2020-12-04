from django.urls import path
from blog.views import AllBlogPosts, OneBlogPost

urlpatterns = [
    path('all_posts/', AllBlogPosts.as_view(template_name='all_posts.html'), name='all-blog-posts'),
    path('all_posts/<int:pk>/', OneBlogPost.as_view(template_name='one_post.html'), name='one-post'),
]