from django.db import models
from django.contrib.auth.models import User

class StandardUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(default="profile1.png", blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    nickname = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.nickname

class Music(models.Model):
    poster = models.ForeignKey(StandardUser, null=True, blank=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=200, blank=True, null=True)
    data = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Requisition(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    about = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField

    standarduser = models.ForeignKey(StandardUser, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.about