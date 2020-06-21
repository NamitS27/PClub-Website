from django.urls import path,include
from .views import resource_list,autocomplete,search

app_name = "resource"

urlpatterns = [
    path('',resource_list,name="resource_list"),
    path('autocomplete/',autocomplete,name="autocomplete"),
    path('search/',search,name="search"),
]