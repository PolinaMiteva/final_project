from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):
    owner = models.OneToOneField(to=User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profiles_pictures', blank=True)

    # def get_absolute_url(self):
    #     return reverse('index', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.owner.username}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


