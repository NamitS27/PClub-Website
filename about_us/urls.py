from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "about_us"

urlpatterns = [
    path('',views.about_us,name="about_us")
]