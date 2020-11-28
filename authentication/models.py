from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):
    owner = models.OneToOneField(to=User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='media/profile_pictures', default='static/images/guest-user.jpg')

