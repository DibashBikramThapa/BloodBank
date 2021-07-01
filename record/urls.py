from django.urls import path
from .import views


app_name= 'record'

urlpatterns=[

    path('',views.HomeView.as_view(),name='Home'),
    path('createhistory/',views.CreateHistoryForm,name='createhistory'),
    path('historylist/',views.HistoryView.as_view(),name='historylist'),
    path('profile/<username>/<int:pk>/',views.ProfileDetailView.as_view(),name='historydetail'),
    path('profile/<username>/<int:pk>/edit',views.HistoryUpdateView.as_view(),name='profileupdate'),
    path('profile/<username>/<int:pk>/delete',views.DeleteHistoryView.as_view(),name='deletehistory'),
    ]
