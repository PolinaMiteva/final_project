from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    header_img = models.ImageField(upload_to='blog_pictures', blank=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    body = models.TextField()
    post_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} | {self.author}'

    # def get_absolute_url(self):
    #     return reverse('all-blog-posts')


class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    comment_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.title} | {self.user.username}'
