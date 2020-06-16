from django.shortcuts import render,get_object_or_404
from .models import Events
from datetime import datetime
# Create your views here.

# def all_events(request):
#     events = Events.objects.all()
#     content = {
#         "events" : events,
#     }
#     return render(request,"event.html",content)

def upcoming_events(request):
    up_events = Events.objects.filter(date__gt=datetime.today())
    eve_type = "Upcoming Events"
    content = {
        "events":up_events,
        "eve_type":eve_type,
    }
    return render(request,"event.html",content)

def live_events(request):
    live_events = Events.objects.filter(date=datetime.today())
    eve_type = "Live Events"
    content = {
        "events":live_events,
        "eve_type":eve_type,
    }
    return render(request,"event.html",content)

def past_events(request):
    past_events = Events.objects.filter(date__lt=datetime.today())
    eve_type = "Past Events"
    content = {
        "events":past_events,
        "eve_type":eve_type,
    }
    return render(request,"event.html",content)


def view_details(request,slug):
    event_obj = get_object_or_404(Events,pk=slug) 
    data = {
        "event" : event_obj,
    }
    return render(request,"page.html",data)