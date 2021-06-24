from django.db import models
from django.contrib.auth.models import User
import datetime
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill,Transpose
from taggit.managers import TaggableManager


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250,null=True)
    contact_number = models.IntegerField(blank=True,null=True)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    added_on =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Us"


WING = [
    
    ('ARMY','ARMY'),
    ('NAVAL','NAVAL'),
    ('AIR FORCE','AIR FORCE')
    
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25,blank=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    image_thumbnail_user = ImageSpecField(source='image',
                                      processors=[Transpose(),ResizeToFill(170, 170)],
                                      format='JPEG',
                                      options={'quality': 100})
    contact_number = models.CharField(max_length=25,blank=True)
    description = models.CharField(max_length=100, blank=True)
    follows = models.ManyToManyField(User,related_name="follows",blank=True)
    followers = models.ManyToManyField(User,related_name="followers",blank=True)
    wing = models.CharField(max_length=15,choices=WING,blank=True)
    def __str__(self):
        return f"{self.user.username}'s Profile"


