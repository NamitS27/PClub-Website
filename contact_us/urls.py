from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "contact_us"

urlpatterns = [
    path('',views.contact_us,name="contact_us")
]