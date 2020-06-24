from django.contrib import admin
from django.urls import path,include
from . import views
# from .. import settings

app_name = "events"

urlpatterns = [
    path('upcoming_events',views.upcoming_events,name="upcoming_events"),
    path('today_events',views.today_events,name="today_events"),
    path('past_events',views.past_events,name="past_events"),
    # path('<slug:slug>',views.view_details,name="view_details"),
]