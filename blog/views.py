from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.forms import CommentForm
from blog.models import Post, Comment


class AllBlogPosts(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'all_posts.html'
    paginate_by = 4


class OneBlogPost(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'one_post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()

    # def get_queryset(self):
    #     if self.request.user.is_authenticated:
    #         return Post.objects.get(pk=self.request["pk"])
    #     else:
    #         return Post.objects.none()
