from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    picture = models.ImageField(default='default_user.png', upload_to='profile_pictures')
    phone_number = models.IntegerField(default='0000')

