from django.shortcuts import render,get_object_or_404
from .models import Events
from datetime import datetime,date,timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upcoming_events(request):
    if request.method =='GET':
        up_events = Events.objects.filter(date__gt=datetime.today()).order_by('date')
        eve_type = "Upcoming Events"
        content = {
            "events":up_events,
            "eve_type":eve_type,
        }
        return render(request,"event.html",content)
    elif request.is_ajax():
        return JsonResponse(view_details(request.POST['id']))

@csrf_exempt
def today_events(request):
    if request.method =='GET':
        today = str(date.today())
        yy = int(today[:4])
        mm = int(today[5:7])
        dd = int(today[9:11])
        startdate = date.today()
        enddate = startdate + timedelta(days=1)
    # Sample.objects.filter(date__range=[startdate, enddate])
        live_events = Events.objects.filter(date__range=[startdate, enddate]).order_by('date')
        eve_type = "Events Today"
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
        past_events = Events.objects.filter(date__lt=datetime.today()).order_by('date')
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

    