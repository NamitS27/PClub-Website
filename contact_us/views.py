from django.shortcuts import render
from other_files import send_email as se
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def contact_us(request):
    if request.method == 'GET':
        return render(request,'contact_us.html')
    elif request.is_ajax():
        # print(request.POST)
        done = se.send(request.POST['name'],request.POST['email'],request.POST['subject'],request.POST['message'],request.POST['jw'])
        return JsonResponse({'done':done})


# Create your views here.
