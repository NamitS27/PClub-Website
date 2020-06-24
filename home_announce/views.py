from django.shortcuts import render
from .models import Announcement,Daily
from datetime import datetime,date,timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import timeago as ta
import pytz
from competitive_programming.models import Contest,PClub_contest
from events.models import Events
# Create your views here.
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
                x['image'] = i.announcement_image
            announcements.append(x)
            cnt += 1
        quest = {}
        try:
            question = Daily.objects.filter(question_tobeadded=date.today())
            ques = None
            for i in question:
                ques = [i.question,i.question_isQuote,i.answer]
            quest['question'] = ques[0]
            quest['isQuote'] = None if ques[1] else "Yes"
            quest['answer'] = ques[2]
        except:
            question = None
        startdate = date.today()
        enddate = startdate + timedelta(days=1)
        events = Events.objects.filter(date__range=[startdate, enddate])
        contests = Contest.objects.filter(contest_start__range=[startdate, enddate])
        pcontests = PClub_contest.objects.filter(contest_start__range=[startdate, enddate])
        content={
            'announce':announcements,
            'upperd':upperd,
            'question':quest,
        }
        if len(events)>0:
            content['new_event'] = "yes"
        if len(contests) + len(pcontests)>0:
            content['contest_today'] = "yes"
        # print(content)
        # print(content)
        return render(request,'home.html',content)
    # else:
    #     if request.is_ajax():
    #         answer = Daily.objects.filter(question = request.POST['question'])
    #         ans = None
    #         for i in answer:
    #             ans = i.answer
    #         return JsonResponse({'ans':ans})



