from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import UserProfile

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("email","username", "password1", "password2",
                "phonenumber","bloodgroup","address")
        model= get_user_model()
