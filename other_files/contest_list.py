import requests,json
import sys
from datetime import *
from dateutil.relativedelta import relativedelta
import pytz
import os


def geturl(site,username=os.environ.get('CLIST_USERNAME'),api_key=os.environ.get('CLIST_API_KEY')): # change username and api-key
    tz = pytz.timezone('UTC')
    date = datetime.now(tz).strftime("%Y-%m-%dT%H:%M:%S")
    final = datetime.today()+ relativedelta(months=1)
    end = final.strftime("%Y-%m-%dT23:59:59")
    try:
        url = "https://clist.by/api/v1/json/contest/?resource__name={}&start__gte={}&end__lt={}&order_by=end&username={}&api_key={}".format(site,date,end,username,api_key)
        response = requests.request("GET",url)
        texting = response.text
        return json.loads(texting)
    except:
        return {'objects':[]}

def change_time(time):
    t1 = time[:10] + " " + time[11:]
    date_object = datetime.strptime(t1, "%Y-%m-%d %H:%M:%S")
    t1d = date_object + timedelta(hours=5, minutes=30)
    return t1d