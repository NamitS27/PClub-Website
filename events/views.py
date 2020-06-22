from django.shortcuts import render,get_object_or_404
from .models import Events
from datetime import datetime
#from datetime import date
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upcoming_events(request):
    if request.method =='GET':
        up_events = Events.objects.filter(date__gt=datetime.today())
        eve_type = "Upcoming Events"
        content = {
            "events":up_events,
            "eve_type":eve_type,
        }
        return render(request,"event.html",content)
    elif request.is_ajax():
        return JsonResponse(view_details(request.POST['id']))

@csrf_exempt
def live_events(request):
    if request.method =='GET':
        live_events = Events.objects.filter(date=datetime.today())
        eve_type = "Live Events"
        content = {
            "events":live_events,
            "eve_type":eve_type,
        }
        return render(request,"event.html",content)
    elif request.is_ajax():
        return JsonResponse(view_details(request.POST['id']))

@csrf_exempt
def past_events(request):
    if request.method =='GET':
        past_events = Events.objects.filter(date__lt=datetime.today())
        eve_type = "Past Events"
        content = {
            "events":past_events,
            "eve_type":eve_type,
        }
        return render(request,"event.html",content)
    elif request.is_ajax():
        return JsonResponse(view_details(request.POST['id']))


def view_details(slug):
    slug = int(slug)
    event = get_object_or_404(Events,pk=slug) 
    # print(type(event_obj))
    image_logo = "/media/"+str(event.logo)
    events = {'name': event.name,'description':event.description,'logo':image_logo,'date':event.date,'can_register':event.can_register,'feedback_link':event.feedback_link,'photos_link':event.photos_link,'registration_date':event.registration_date,'registration_link':event.registration_link}
    data = {
        "event" : events,
    }
    return data

    