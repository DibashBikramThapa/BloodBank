from django.shortcuts import render
from django.contrib.auth import login, logout
from . import forms

def SignUp(request):

    registered = False

    if request.method == "POST":
        user_form=forms.UserCreateForm(data=request.POST)
        donor_form=forms.DonorForm(data=request.POST)

        if user_form.is_valid() and donor_form.is_valid():
            user=user_form.save()
            user.save()
            donor=donor_form.save(commit=False)
            donor.user=user
            donor.save()
            registered=True
        else:
            print(user_form.errors, donor_form.errors)
    else:
        user_form=forms.UserCreateForm()
        donor_form=forms.DonorForm()

    context={
            'registered':registered,
            'user_form':user_form,
            'donor_form':donor_form,


            }
    return render(request,"signup.html",context)
