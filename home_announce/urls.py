from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "home_announce"

urlpatterns = [
    path('',views.make_announce,name="make_announce")
]