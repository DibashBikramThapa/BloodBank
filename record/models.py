from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.urls import reverse
from accounts.models import UserProfile
from django.contrib.auth import get_user_model
User = get_user_model()

class History(models.Model):
    user=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    lastdonateddate = models.DateField(default=timezone.now(), blank=True)

    def get_absolute_url(self):
        return reverse(
                        "record:historylist")


    def __str__(self):
        return self.user.username
