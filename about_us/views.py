from django.shortcuts import render
from .models import Member,About
# Create your views here.

def about_us(request):
    about = About.objects.all()
    members = Member.objects.all()
    content = {
        'about':about,
        'members':members
    }
    return render(request,'about_us.html',content)