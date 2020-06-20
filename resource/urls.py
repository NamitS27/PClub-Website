from django.urls import path,include
from .views import resource_list

app_name = "resource"

urlpatterns = [
    path('',resource_list,name="resource_list")
]