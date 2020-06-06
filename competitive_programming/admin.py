from django.contrib import admin
from .models import Server_time,Platform,Contest
# Register your models here.

admin.site.register(Platform)
admin.site.register(Contest)
admin.site.register(Server_time)

