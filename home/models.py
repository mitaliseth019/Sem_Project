from django.db import models
from django.contrib.auth.models import User
import datetime



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



class register_table(models.Model):
    cat =(
    ("1", "Fashion"),
    ("2", "Food"),
    ("3", "Music"),
    ("4", "Art"),
    ("5", "Lifestyle"),
)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contact_number = models.IntegerField()
    profile_pic =models.ImageField(upload_to = "profiles/%Y/%m/%d",null=True,blank=True)
    age = models.CharField(max_length=250,null=True,blank=True)
    city = models.CharField(max_length=250,null=True,blank=True)
    about = models.TextField(blank=True,null=True)
    youtube= models.URLField(max_length=250, blank=True)
    instagram= models.URLField(max_length=250, blank=True)
    facebook= models.URLField(max_length=250, blank=True)
    snapchat = models.URLField(max_length=250, blank=True,null=True)
    cat1 = models.CharField(max_length=250,null=True,blank=True, choices=cat)
    cat2 = models.CharField(max_length=250,null=True,blank=True, choices=cat)
    cat3 = models.CharField(max_length=250,null=True,blank=True, choices=cat)
    added_on =models.DateTimeField(auto_now_add=True,null=True)
    update_on = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.user.username

