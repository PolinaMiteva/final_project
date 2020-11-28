from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    owner = models.OneToOneField(to=User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profiles_pictures')

    # def get_absolute_url(self):
    #     return reverse('index', kwargs={'pk': self.pk})


