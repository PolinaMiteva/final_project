from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

UserModel = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_img = models.ImageField(upload_to='blog_pictures', blank=True)
    author = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)
    body = models.TextField()
    post_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} | {self.title}'


class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    comment_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} | {self.post.title}'
