from django.shortcuts import render, redirect
from donation_app.models import Contactform
from django.core.mail import send_mail
# Create your views here.
def index(request):
    data={
        "title":"Sparks Donation"
    }
    return render(request,'index.html',data)
def about(request):
    data={
        "title":"Sparks Donation : AboutUs"
    }
    return render(request,'about.html',data)
def contact(request):
    data={
        "title":"Sparks Donation : ContactUS",
    }
    try:
        if request.method=="POST":
            d1=request.POST.get('name')
            d2=request.POST.get('email')
            d3=request.POST.get('subject')
            d4=request.POST.get('message')
            btn=request.POST.get('submit')
            details = Contactform(
                Name = d1,
                Email = d2,
                Subject = d3,
                Message = d4
            )
            details.save()
            send_mail(
                d2,
                d4 + "\n Sender\n"+d1+"\n"+d2,
                "nullnftworld@gmail.com",
                ["satyak0330@gmail.com"],
                fail_silently=False,
            )
            return redirect('thankyou')
    except:
        pass
    return render(request,'contact.html',data)

def thankyou(request):
    data={
        "title":"Sparks Donation : Thanks"
    }
    return render(request,'thankyou.html',data)