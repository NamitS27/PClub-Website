from django.shortcuts import render
from .models import Member,About

def about_us(request):
    about = About.objects.all()
    abt = None
    for ab in about:
        abt = ab
    members = Member.objects.all()
    content = {
        'abt':abt,
        'members':members
    }
    return render(request,'about_us.html',content)