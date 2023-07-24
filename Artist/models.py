from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.urls import reverse


class ArtistProfile(models.Model):
    nickname = models.OneToOneField(to=User, on_delete=models.CASCADE)
    picture  = CloudinaryField('ProfilePicture', default='defaultimage.jpg')

    def __str__(self) -> str:
        return super().__str__() +' of '+ str(self.nickname)
    
    def get_absolute_url(self):
        return reverse('viewall')
    
    