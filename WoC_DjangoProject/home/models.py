from django.db import models
from django.db.models.deletion import CASCADE
import imp
from dotenv import load_dotenv
import os
from twilio.rest import Client

# Create your models here.
# class sending(models.Model):
class Event_Registration(models.Model):
    nEvent = models.CharField( max_length=122,default = "")
    name = models.CharField( max_length=122,default = "")
    # lname = models.CharField( max_length=122,default = "")
    desc = models.TextField( max_length=122,default = "")
    location = models.CharField( max_length=122,default = "")
    stime = models.DateTimeField( auto_now=False, auto_now_add=False)
    etime = models.DateTimeField(auto_now=False, auto_now_add=False)
    deadline = models.DateField(auto_now=False, auto_now_add=False)
    host_email = models.EmailField(max_length=244,default="",null=True)
    password = models.CharField(max_length=50)
    nop = models.IntegerField(default="0")

# class load(models.Model):
class Participant_Registration(models.Model):
    fname = models.CharField( max_length=122,default = "")
    lname = models.CharField( max_length=122,default = "")
    num = models.CharField(max_length=10,default = "")
    email = models.EmailField(max_length=244,default="")
    password = models.CharField(max_length=122,default="")
    nopar = models.CharField( max_length=10,default="1")
    nevent = models.CharField(max_length=122)

    def save(self, *args, **kwargs):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body='Hello There, You have successfully registered in the Event.',
            from_=os.environ['MY_NUM1'],
            to=os.environ['MY_NUM2'],#num
            # to='+91'+args[0],#num
        )
        
        return super().save(*args, **kwargs)
    