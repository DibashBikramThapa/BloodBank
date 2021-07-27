# About Bloodproject
This is a record of donor where blooddonor are listed in a table in UI viewed by anyone. The tale shows:
* Email (required)
* Username (required)
* Bloodgroup (in choice form)
* Address
* Phone number

## BACKEND of project
Account and record, two apps are used for my project named bloodproject to achieve real project scenario.
* #### Models
  1. Account
    > Here using AbstractBaseUser, BaseUserManager from django.contrib.auth.models,
      and changing USERNAME_FIELD to 'email', login through email is achieved.

    >  Then from django.contrib.auth, django.contrib.auth.forms, (get_user_model, UserCreationForm) are imported for signup.
    >  For login/logout, auth_views LoginView and LogoutView are used.
  2. Record
    >  Here simply, class named History is made to record the lastdonateddate which uses timezone.now() from django.utils.

* #### Views
  ```
   1. The CRUD function form django.views.generic, ListView, CreateView, DetailView, UpdateView, DeleteView is acheieved with LoginRequiredMixin, SelectRelatedMixin from django.contrib.auth.mixins and braces.views.

   2. To filter the user for create, edit and delete, queryset used is
      def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

  3. To search code used is:
      def get_queryset(self):
          query = self.request.GET.get('q')
          return UserProfile.objects.filter(
                          s(bloodgroup__icontains=query) | s(address__icontains=query)
                          )
      where get('q') gets the name ='q' written in search form.
    ```

## Front End
```
1. In mainbase.html from templates folder of base directory, UI of nav bar, image top, left and right is done using column, row class with margin, padding as required for index page, list page.

2. In base.html from templates folder of record app, UI of nav bar is used for signup, login and history list. Here I could have made seperate navbar.html, image.html to include but i haven't learned it.
```
## Database
> I have tried with mysql in local development but since in heroku bug occured, default sqlite3 is used for database.


## To run
* [Bloodproject click me!](https://blooddonorsystem.herokuapp.com)
```
For admin:
  1. login- email: funky@gmail.com
            pw:funky@123
```
### Project SS

* Homepage: ![Homepage](/home/funky/Desktop/practise/copy/copyBloodSystem/BloodProjectSS/Homepage.png)

* Signup: ![signup](/home/funky/Desktop/practise/copy/copyBloodSystem/BloodProjectSS/Signup.png)

* Login: ![login](/home/funky/Desktop/practise/copy/copyBloodSystem/BloodProjectSS/Login.png)

* Enter last donated date: ![date](/home/funky/Desktop/practise/copy/copyBloodSystem/BloodProjectSS/date.png)

* History list: ![History list](/home/funky/Desktop/practise/copy/copyBloodSystem/BloodProjectSS/historylist.png)

* Edit/Update: ![edit](/home/funky/Desktop/practise/copy/copyBloodSystem/BloodProjectSS/update.png)

* Delete: ![delete](/home/funky/Desktop/practise/copy/copyBloodSystem/BloodProjectSS/delete.png)
