from django.urls import path
from .import views


app_name= 'record'

urlpatterns=[

    path('',views.HomeView.as_view(),name='Home'),
    path('createhistory/',views.CreateHistoryForm,name='createhistory'),
    path('historylist/',views.HistoryView.as_view(),name='historylist'),

    ]
