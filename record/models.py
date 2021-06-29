from django.db import models
from django.contrib import auth
from django.utils import timezone
from accounts.models import Donor

class History(models.Model):
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    lastdonateddate = models.DateField(default=timezone.now())

    def __str__(self):
        return self.user.username
