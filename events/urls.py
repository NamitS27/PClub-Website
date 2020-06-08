from django.contrib import admin
from django.urls import path,include
from . import views
# from .. import settings

app_name = "events"

urlpatterns = [
    path('',views.all_events,name="all_events"),
    path('<slug:slug>',views.view_details,name="view_details"),
]