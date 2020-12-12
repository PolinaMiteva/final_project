from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, FormView, CreateView

from Django_fnl_project.decorators import required_user, required_user_for_comment, required_group_user
from Django_fnl_project.mixins import GroupRequiredMixin
from blog.forms import CommentForm, PostForm
from blog.models import Post, Comment


class AllBlogPosts(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'all_posts.html'
    paginate_by = 2
    ordering = 'post_datetime'


@login_required
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


@login_required
@required_user_for_comment
def edit_comment(request, pk):
    if request.method == "POST":
        instance = Comment.objects.get(pk=pk)
        current_body = instance.body
        form = CommentForm(request.POST, instance=instance,)
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


@login_required
@required_user_for_comment
def delete_comment(request, pk):
    if request.method == "POST":
        instance = Comment.objects.get(pk=pk)
        instance.delete()
        next = request.GET.get('next', reverse('all-blog-posts'))
        return HttpResponseRedirect(next)

    elif request.method == "GET":
        return render(request, 'delete_comment.html')


class NewPostView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'new_post.html'
    success_url = reverse_lazy('all-blog-posts')
    groups = ['writers']

    def get_context_data(self, **kwargs):
        context = super(NewPostView, self).get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', reverse('index'))
        return context



@login_required
@required_group_user
def edit_post(request, pk,):
    if request.method == "GET":
        instance = Post.objects.get(pk=pk)
        context = {
            'form': PostForm(instance=instance),
            'next': request.GET.get('next', reverse('all-blog-posts')),
        }
        return render(request, 'edit_post.html', context)

    elif request.method == "POST":
        instance = Post.objects.get(pk=pk)
        form = PostForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            next = request.GET.get('next', reverse('all-blog-posts'))
            return HttpResponseRedirect(next)

    context = {
        'form': PostForm(request.POST, instance=instance),
    }
    return render(request, 'edit_post.html', context)


