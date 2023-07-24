from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ArtistProfile


@receiver(post_save, sender=User)
def make_a_profile_automatically(sender, instance, created, **kwargs):
    if created:
        ArtistProfile.objects.create(nickname=instance)
        print('******** profile created')


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.artistprofile.save()
        print('*******profile updated')

