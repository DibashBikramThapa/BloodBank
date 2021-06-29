from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import Donor
from django.contrib import auth

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"

class DonorForm(forms.ModelForm):
    class Meta():
        fields=['email','bloodgroup','phonenumber','address']
        model = Donor
