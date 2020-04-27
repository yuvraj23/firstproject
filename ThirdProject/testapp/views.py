from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def timeinfo(request):
    date=datetime.datetime.now()
    x=int(date.strftime("%H"))
    x=x+20
    msg="<h1><center>This is Yuvraj And I welcome to my website"
    msg=msg+" And wishing u a very "
    if x<12:
        msg=msg+" Gud morning"
    elif x<16:
        msg=msg+" Gud Afternooon"
    elif x < 21:
        msg=msg+" Gud evening"
    else:
        msg=msg+" Gud Night"
    msg=msg+" At server time"+"  "+str(date)+"    - > "+str(x)+ "</center></h1>"
    return HttpResponse(msg)
