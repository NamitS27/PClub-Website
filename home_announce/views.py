from django.shortcuts import render
from .models import Announcement
from datetime import datetime
import timeago as ta
import pytz
# Create your views here.
def make_announce(request):
    announcement = Announcement.objects.all()
    upperd = []
    print(len(announcement))
    for i in range(len(announcement)):
        x = {}
        x['id'] = i
        if i==0:
            x['class']='active'
        upperd.append(x)
    announcements = []
    cnt = 0
    tz = pytz.timezone('Asia/Kolkata')
    for i in announcement:
        x = {}
        if i.announcement_isActive:
            x['sr'] = cnt
            x['title'] = i.announcement_title
            x['date'] = ta.format(i.announcement_date,datetime.now(tz))
            x['description'] = i.announcement_description
            x['image'] = i.announcement_image
        announcements.append(x)
        cnt += 1
    content={
        'announce':announcements,
        'upperd':upperd,
    }
    print(content)
    return render(request,'home.html',content)

