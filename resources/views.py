from django.shortcuts import render
from .models import Resource,Resource_link
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def list_resources(request):
    if request.method == "GET":
        resource = Resource.objects.all()
        # links = {}
        # for ind_resource in resource:
        #     x = Resource_link.objects.filter(resource_link_id__id=ind_resource.id)
        #     links[ind_resource.resource_topic] = []
        #     for ind_links in x:
        #         links[ind_resource.resource_topic].append([ind_links.resource_link,ind_links.resource_link_type])
        content = {
            'resource':resource,
            # 'links':links
        }
        return render(request,'resources.html',content)
    elif request.is_ajax():
        resource_name = request.POST['name']
        resource = Resource.objects.filter(resource_topic = resource_name)
        resid = None
        for i in resource:
            resid = i.id
        x = Resource_link.objects.filter(resource_link_id__id=resid)
        links = [{'type':il.resource_link_type,'link':il.resource_link} for il in x]
        return JsonResponse({'links':links})
            # links[ind_resource.resource_topic].append([ind_links.resource_link,ind_links.resource_link_type])

# Create your views here.
