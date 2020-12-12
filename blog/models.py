from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    slug = models.SlugField(
        editable=False,
    )
    title = models.CharField(max_length=255)
    header_img = models.ImageField(upload_to='blog_pictures', blank=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    body = models.TextField()
    post_datetime = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.author} | {self.title}'


class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    comment_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.title} | {self.body}'
