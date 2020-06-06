from django.shortcuts import render,get_object_or_404
from .models import Events
# Create your views here.

def all_events(request):
    events = Events.objects.all()
    content = {
        "events" : events,
    }
    texxt = "red"
    return render(request,"event.html",content)

def view_details(request,slug):
    event_obj = get_object_or_404(Events,pk=slug) 
    data = {
        "event" : event_obj,
    }
    return render(request,"page.html",data)