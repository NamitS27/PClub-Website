from django.contrib import admin
from django.urls import path,include
from .views import contest,show_contest

app_name = "comptetitive_programming"

urlpatterns = [
    path('',contest,name="contest"),
    path('<int:v>',show_contest,name="show_contest"),
]
