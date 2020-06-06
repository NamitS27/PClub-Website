from django.contrib import admin
from .models import Events
from django_summernote.admin import SummernoteModelAdmin   

class EventAdmin(SummernoteModelAdmin):
    summernote_feilds = ('description',)

# admin.site.register(Events)
admin.site.register(Events,EventAdmin)