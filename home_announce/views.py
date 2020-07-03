from django.shortcuts import render
from .models import Announcement,Daily
from datetime import datetime,date,timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import timeago as ta
import pytz
from competitive_programming.models import Contest,PClub_contest
from events.models import Events

@csrf_exempt
def make_announce(request):
    if request.method =='GET':
        announcement = Announcement.objects.all()
        upperd = []
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
                x['isevent'] = "Yes" if i.announcement_isofEvent else None
            if len(x)>0:
                announcements.append(x)
            cnt += 1
        quest = {}
        try:
            question = Daily.objects.filter(question_tobeadded__day=date.today().day)
            ques = None
            for i in question:
                # print(i.question_isQuote)
                ques = [i.question,i.question_isQuote,i.answer]
            # print(ques)
            quest['question'] = ques[0]
            quest['isQuote'] = None if ques[1] else "Yes" # Logic is set as per the html file
            quest['answer'] = ques[2]
            quest['not_found'] = "Yes" # logic is set as per the html file
        except:
            quest['not_found'] = None # Logic is set as per the html file
        startdate = date.today()
        enddate = startdate + timedelta(days=1)
        events = Events.objects.filter(date__range=[startdate, enddate])
        contests = Contest.objects.filter(contest_start__range=[startdate, enddate])
        pcontests = PClub_contest.objects.filter(contest_start__range=[startdate, enddate])
        content={
            'announce':announcements,
            'any_announcements': "Yes" if len(announcements)>0 else None,
            'upperd':upperd,
            'question':quest,
        }
        # print(quest)
        if len(events)>0:
            content['new_event'] = "yes"
        if len(contests) + len(pcontests)>0:
            content['contest_today'] = "yes"
        return render(request,'home.html',content)



