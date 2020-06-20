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

