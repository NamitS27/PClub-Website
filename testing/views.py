from django.shortcuts import render

# Create your views here.
def test(request):
    content = {
        'events':[["Suhanee","26th May,2020","/media/images/0.jpg"],["Suhanee","26th May,2020","/media/images/Encryption.png"],["Suhanee","26th May,2020","/media/images/Encryption.png"],["Suhanee","26th May,2020","/media/images/Encryption.png"],["Suhanee","26th May,2020","/media/images/Encryption.png"]]
    }
    return render(request,"test.html",content)