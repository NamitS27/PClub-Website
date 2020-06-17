from django.shortcuts import render
from .models import Announcement
# Create your views here.
def make_announce(request):
    announcement = Announcement.objects.all()
    content={
        'announce':announcement
    }
    return render(request,'home.html',content)
