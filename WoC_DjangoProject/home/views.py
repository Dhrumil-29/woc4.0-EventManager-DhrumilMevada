from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime
from home.models import Event_Registration
from home.models import Participant_Registration
from django.core.mail import send_mail
from dotenv import load_dotenv 
import os
load_dotenv()

# Create your views here.
def home(request):
    return render(request,"Home.html")

def index(request):
    return render(request,"Home.html")


def participant_list(request):
    if request.method == "POST": 
        if Participant_Registration.objects.all().filter(nevent=request.POST.get('eventid')).exists():
                context = {'participant_list': Participant_Registration.objects.all().filter(nevent=request.POST.get('eventid'))}
                # print(context)
                return render(request,'participant_list.html',context)  
        else:
            context = {'messages':"Event Name is incorrect !"}
            return render(request, 'participant_list.html', context)

def login(request):
    if request.method == "POST": 
        
        hostid = request.POST.get('hostid')
        password = request.POST.get('password')

        # if request.POST.get('person') == 'Host':
        if Event_Registration.objects.all().filter(host_email=hostid,password=password).exists():# and Event_Registration.objects.get(host_email=hostid).password == password:
            context = {'event_list': Event_Registration.objects.all().filter(host_email=hostid),'allowed':'yes'}
            # print(context)
            return render(request,'loginpage.html',context)  
        else:
            context = {'messages':"Username or password is incorrect !"}
            return render(request, 'loginpage.html', context)
        # else:
        #     if  Participant_Registration.objects.all().filter(email=hostid).exists() and Participant_Registration.objects.get(email=hostid).password == password:
        #         context = {'part_list': Participant_Registration.objects.all().filter(email=hostid)}
        #         return render(request, 'loginpage.html',context) 
        #     else:
        #         context = {'messages':"Username or password is incorrect !"}
        #         return render(request, 'loginpage.html', context)

        return render(request,"loginpage.html")
    else:
        return render(request,"loginpage.html",{'allowed':'no'})
        

def event_detail(request):
    event_list = Event_Registration.objects.all().filter(deadline__gte = datetime.now())
    return render(request,"Event Details.html",{'event_list' : event_list})

def event_registration(request):
    if request.method == "POST":
        nEvent = request.POST.get('nEvent')
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        location = request.POST.get('location')
        stime = request.POST.get('stime')
        etime = request.POST.get('etime')
        deadline = request.POST.get('deadline')
        host_email = request.POST.get('host_email')
        password = request.POST.get('password')

        if stime > etime or deadline>stime:
            context = {'message' : 'Invalid data inserted'}
            return render(request, 'Event Registration.html', context)

        event = Event_Registration(nEvent=nEvent ,name=name, desc = desc, location=location,stime=stime,etime=etime,deadline=deadline, host_email=host_email,password=password)

        if Event_Registration.objects.all().filter(host_email=host_email, nEvent=nEvent):
            context = {'message' : "You have already Registrated This Event !!!"}
            return render(request, 'Event Registration.html', context)
        event.save()

        send_mail(
           'Event : ' + nEvent,#Subject
            'Here is The Confirmation Message.\n Good Luck !',#message
            os.environ.get("email_user"),#from
            [host_email],#to
            fail_silently=False,
        )
    return render(request,"Event Registration.html")


def participant_registration(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        num = request.POST.get('num')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if request.POST.get('person') == 'Individual':
            nopar = 1
        else:
            nopar = request.POST.get('nopar')
            if nopar < '2':
                context = {'message' : "You have enter invaild No. of Participants Value...!!!"}
                return render(request, 'Participant Registration.html', context)

        nevent = request.POST.get('nevent')
        if Event_Registration.objects.all().filter(deadline__gte = datetime.now(),nEvent=nevent):
        # if Event_Registration.objects.all().filter(nEvent=nevent):
            pass
        else:
            context = {'message' : "You have Entered Invaild Event Name...Please Check Event Name From Event Details Section...!!!"}
            return render(request, 'Participant Registration.html', context)

        if Participant_Registration.objects.all().filter(email=email, nevent=nevent):
            context = {'message' : "You have already participated in the event !"}
            return render(request, 'Participant Registration.html', context)

        event1 = Participant_Registration(fname=fname,lname=lname,num=num,email=email,password=password,nopar=nopar,nevent=nevent)

        for i in Event_Registration.objects.all().filter(nEvent = nevent):
                i.nop = i.nop + int(nopar)
                i.save()
        # event1.save(num,num)
        event1.save()
        
    return render(request,"Participant Registration.html")