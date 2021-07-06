from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager


Blood_Group=(
    ('A+','A+'),
    ('B+','B+'),
    ('O+','O+'),
    ("AB+","AB+"),

)


class UserProfileManager(BaseUserManager):
    """manager user profiles"""

    def create_user(self, email, username, password=None):
        """create user prof"""
        if not email:
            raise ValueError("Email is must")

        email=self.normalize_email(email)
        user = self.model(email=email, username=username)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        """create superuser"""
        user = self.create_user(email,username,password)
        user.is_superuser=True
        user.is_staff= True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """user database model"""
    email=models.EmailField(max_length=200, unique=True)
    username=models.CharField(max_length=10,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    bloodgroup=models.CharField(choices=Blood_Group,max_length=3)
    phonenumber=models.CharField(max_length=10,unique=True)
    address = models.CharField(max_length=264)

    objects = UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    def get_full_name(self):
        return self.username

    def __str__(self):
        return self.email
