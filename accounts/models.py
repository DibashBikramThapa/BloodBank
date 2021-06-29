from django.db import models
from django.contrib import auth
from django.utils import timezone

Blood_Group=(
    ('A+','A+'),
    ('B+','B+'),
    ('O+','O+'),
    ("AB+","AB+"),

)


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return self.username


class Donor(models.Model):
    user=models.OneToOneField('auth.User',on_delete=models.CASCADE)
    email=models.EmailField(unique=True)
    bloodgroup=models.CharField(choices=Blood_Group,max_length=3)
    phonenumber=models.CharField(max_length=10,unique=True)
    address = models.CharField(max_length=264)

    def __str__(self):
        return self.user.username
