from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    
    path("home", views.home, name='home'),
    
    path("event_detail", views.event_detail, name='event_detail'),

    path("login", views.login, name='login'),
    
    path("event_registration", views.event_registration, name='event_registration'),
    
    path("participant_registration", views.participant_registration, name='participant_registration'),

    path("participant_list", views.participant_list, name='participant_list')
]