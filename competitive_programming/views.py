from django.shortcuts import render
from other_files import contest_list as cl
from other_files import suggest_problems as sp
from datetime import datetime,timezone,timedelta
from .models import Platform,Contest,Server_time,PClub_contest
from dateutil.relativedelta import relativedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import time
import pytz

tz = pytz.timezone("Asia/Kolkata")

def empty_table():
    st = Server_time.objects.all()
    for i in st:
        i.delete()
    contests = Contest.objects.all()
    for i in contests:
        i.delete()
    platforms = Platform.objects.all()
    for i in platforms:
        i.delete()

def define_table():
    empty_table()
    site = [["codeforces.com","CODEFORCES"],["codechef.com","CODECHEF"],["atcoder.jp","ATCODER"],["topcoder.com","TOPCODER"],["hackerearth.com","HACKEREARTH"],["codingcompetitions.withgoogle.com","GOOGLE"],["hackerrank.com","HACKERRANK"]]
    for eacheve in site:
        cnt = 1
        pt = Platform()
        pt.platform_name = eacheve[1]
        pt.platform_link = eacheve[0]
        pt.save()
        for event in cl.geturl(eacheve[0])['objects']:
            events = []
            cnt += 1
            duration = str(timedelta(seconds=event['duration']))
            # print(cl.change_time(event['start']),cl.change_time(event['end']))
            start,end = cl.change_time(event['start']),cl.change_time(event['end'])
            name = event['event']
            link = event['href']
            cts = Contest(contest_name=name,contest_duration=duration,contest_start=start,contest_end=end,contest_link=link,contest_id=pt)
            cts.save()
    st = Server_time()
    st.server_update_time = datetime.now(tz)
    st.save()

@csrf_exempt
def contest(request):
    if request.method == 'GET':
        get_time = Server_time.objects.all()
        ser_tm = None
        for t in get_time:
            ser_tm = t.server_update_time
        time_interval = int((datetime.now(tz)-ser_tm).total_seconds())
        # print(time_interval)
        if time_interval>10000:
            define_table()
        return render(request,'cp_reloaded.html')
    elif request.is_ajax():
        if request.POST['choose']=="contests":
            cid = int(request.POST['id'])
            # print(cid)
            if cid>1:
                platform_name,contests = get_contest(cid)
                contest = [{'name': cont.contest_name, 'start': str(cont.contest_start + timedelta(hours=5, minutes=30))[:19],'end':str(cont.contest_end + timedelta(hours=5, minutes=30))[:19],'duration':cont.contest_duration,'link':cont.contest_link} for cont in contests]
                content ={
                    'platform':platform_name,
                    'contest':contest,
                    # 'number_of_contest':len(contest),
                }
                # print(contest)
            else:
                contests = PClub_contest.objects.all();
                contest = [{'platform':eachc.platform_name,'name':eachc.contest_name,'duration':eachc.contest_duration,'start':eachc.contest_start.strftime("%Y-%m-%d %H:%M:%S"),'end':eachc.contest_end.strftime("%Y-%m-%d %H:%M:%S"),'link':eachc.contest_link} for eachc in contests]
                content = {
                    'contest':contest,
                }
            print(content)
            return JsonResponse(content)
        else:
            r1 = int(request.POST['min'])
            r2 = int(request.POST['max'])
            cf = request.POST['username']
            tag = request.POST['tag']
            prob = sp.get_problems(r1,r2,cf,tag)
            return JsonResponse({'prob':prob})


def get_contest(which_contest):
    arr = ["CODECHEF","CODEFORCES","ATCODER","HACKERRANK","HACKEREARTH","GOOGLE","TOPCODER"]
    plat = Platform.objects.filter(platform_name=arr[which_contest-2])
    platform = None
    for i in plat: platform = i
    contests = Contest.objects.filter(contest_id__id=platform.id)
    return platform.platform_name,contests


def show_contest(request,v):
    platform_name,contests = get_contest(v)
    content ={
        'con':contests,
        'platform':platform_name
    }
    return render(request,"contest.html",content)


    