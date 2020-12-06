from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
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


@login_required()
def one_blog_post(request, pk):
    if request.method == 'POST':
        Comment.objects.create(
            user=request.user,
            post=Post.objects.get(pk=pk),
            body=request.POST['body'],
        )
        return redirect('one-post', pk)

    post = Post.objects.get(pk=pk)
    all_comments = Comment.objects.filter(post_id=pk)
    comment_form = CommentForm()

    context = {
        'post': post,
        'comment_form': comment_form,
        'all_comments': all_comments,
    }

    return render(request, 'one_post.html', context)


@login_required()
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


@login_required()
def delete_comment(request, pk):
    if request.method == "POST":
        instance = Comment.objects.get(pk=pk)
        instance.delete()
        next = request.GET.get('next', reverse('all-blog-posts'))
        return HttpResponseRedirect(next)

    elif request.method == "GET":
        return render(request, 'delete_comment.html')

