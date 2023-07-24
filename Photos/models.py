from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from cloudinary.models import CloudinaryField



class Category(models.Model):
    category_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return self.category_name
    
    def get_absolute_url(self):
        return reverse('gallery')


class Shot(models.Model):
    image       = CloudinaryField('MyClicks', null=False, blank=False)
    camera_man  = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    category    = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True, blank=True)
    title       = models.CharField(max_length=100)
    uploaded_on = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return super().__str__() + str(self.title)
    
    def get_absolute_url(self):
        return reverse('gallery')