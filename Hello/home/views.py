from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        'variable':"Sapna is great"
    }
    return render(request,'index.html',context)
    #return HttpResponse("This is homepage")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is about page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("This is services page")

def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        contact = Contact(name=name,email=email,phone=phone,message=message,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request,'contact.html')
    #return HttpResponse("This is contact page")

def packages(request):
    return render(request,'packages.html')
    #return HttpResponse("This is contact page")