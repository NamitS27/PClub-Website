from django.shortcuts import render
from .models import Resource,Resource_link

def list_resources(request):
    resource = Resource.objects.all()
    links = {}
    for ind_resource in resource:
        x = Resource_link.objects.filter(resource_link_id__id=ind_resource.id)
        links[ind_resource.resource_topic] = []
        for ind_links in x:
            links[ind_resource.resource_topic].append([ind_links.resource_link,ind_links.resource_link_type])
    content = {
        'resource':resource,
        'links':links
    }
    return render(request,'resources.html',content)

# Create your views here.
