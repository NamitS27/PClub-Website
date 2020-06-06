from django.urls import path,include
from . import views

app_name = "resources"

urlpatterns = [
    path('',views.list_resources,name="list_resources")
]