from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView

from blog.forms import CommentForm
from blog.models import Post, Comment


class AllBlogPosts(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'all_posts.html'
    paginate_by = 4


def one_blog_post(request, pk):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('one-post', kwargs={'pk': pk})

    post = Post.objects.get(pk=pk)
    all_comments = Comment.objects.filter(post_id=pk)
    comment_form = CommentForm()

    context = {
        'post': post,
        'comment_form': comment_form,
        'all_comments': all_comments,
    }

    return render(request, 'one_post.html', context)


def edit_comment(request, pk):
    if request.method == "POST":
        instance = Comment.objects.get(pk=pk)
        current_body = instance.body
        form = CommentForm(request.POST, instance=instance)
        if form.data['body'] != current_body:
            body = form.data['body']
            instance.body = body
        instance.save()
        next = request.GET.get('next', reverse('all-blog-posts'))
        return HttpResponseRedirect(next)

    elif request.method == "GET":
        form = CommentForm(instance=Comment.objects.get(pk=pk))
        return render(request, 'edit_comment.html', context={'form': form})

    form = CommentForm(request.POST, instance=Comment.objects.get(pk=pk))
    return render(request, template_name=edit_comment, context={'form': form})


def delete_comment(request, pk):
    pass
