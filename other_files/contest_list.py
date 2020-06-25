import requests,json
import sys
from datetime import *
from dateutil.relativedelta import relativedelta
import pytz
import os


def geturl(site,username='noreply9',api_key='6faa6c9be710c1bd97238ac97922b7f7dcf3cd73'): # change username and api-key
    tz = pytz.timezone('UTC')
    date = datetime.now(tz).strftime("%Y-%m-%dT%H:%M:%S")
    final = datetime.today()+ relativedelta(months=1)
    end = final.strftime("%Y-%m-%dT23:59:59")
    url = "https://clist.by/api/v1/json/contest/?resource__name={}&start__gte={}&end__lt={}&order_by=end&username={}&api_key={}".format(site,date,end,username,api_key)
    response = requests.request("GET",url)
    texting = response.text
    return json.loads(texting)

def change_time(time):
    t1 = time[:10] + " " + time[11:]
    date_object = datetime.strptime(t1, "%Y-%m-%d %H:%M:%S")
    t1d = date_object + timedelta(hours=5, minutes=30)
    return t1d