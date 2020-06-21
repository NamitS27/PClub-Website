from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Resource,ResourceLinks

@csrf_exempt
def resource_list(request):
    if request.method == "GET":
        resource = Resource.objects.all()
        content = {
            'resource':resource,
        }
        return render(request,'resources.html',content)
    elif request.is_ajax():
        resource_name = request.POST['name']
        resource = Resource.objects.filter(resource_name = resource_name)
        resid = None
        for i in resource:
            resid = i.id
        x = ResourceLinks.objects.filter(rlink_id__id=resid)
        links = [{'type':il.rtype,'link':il.rlink,'desc':il.rdesp} for il in x]
        return JsonResponse({'links':links})

@csrf_exempt
def search(request):
    if request.is_ajax():
        topic = request.POST['topic']
        if len(topic)>0:
            resource = Resource.objects.filter(resource_name=topic)
        else:
            resource = Resource.objects.all()
        topics = []
        for i in resource:
            topics.append([i.resource_name,i.id])
        data={
            'topic':topics,
        }
        return JsonResponse(data)

@csrf_exempt
def autocomplete(request):
    if request.is_ajax():
        queryset = Resource.objects.filter(resource_name__startswith=request.GET.get('search',None))
        list = []
        for i in queryset:
            list.append(i.resource_name)
        data = {
            'list':list,
        }
        return JsonResponse(data)