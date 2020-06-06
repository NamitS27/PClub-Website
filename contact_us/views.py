from django.shortcuts import render
from other_files import send_email as se

def contact_us(request):
    if request.method == 'GET':
        return render(request,'contact_us.html')
    else:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        # se.send(name,email,subject,message)
        sent = ""
        try:
            sent = request.POST['jw']
        except:
            sent = "No"
        se.send(name,email,subject,message,sent)
        return render(request,'contact_us.html')


# Create your views here.
