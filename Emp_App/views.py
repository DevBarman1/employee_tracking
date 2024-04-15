from django.shortcuts import render
from Emp_App.models import *


# Create your views here.

def index(request):
    dc = DemoContent.objects.all()
    fi = FeaturedIn.objects.all()
    tes = ThreeEasySteps.objects.all()
    tesi = ThreeEasyStepsIcons.objects.all()
    testimonial = Testimonial.objects.all()
    testimonial_slider = TestimonialSlider.objects.all()
    
    
    data = {
        'dc_key':dc,
        'fi_key':fi,
        'tes_key':tes,
        'tesi_key':tesi,
        'testimonial_key':testimonial,
        'testimonial_slider_key':testimonial_slider,
    }
    
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        mail = request.POST['mail']
        phone = request.POST['phone']
        var = ScheduleDemoForm(firstname=firstname,lastname=lastname,mail=mail,phone=phone)
        var.save()
    return render(request,"index.html",data)

def employeeMonitering(request):
    return render(request,"EmployeeMonitering.html")

def fieldTracking(request):
    return render(request,"FieldTracking.html")

def pricing(request):
    return render(request,"Pricing.html")

def workforce_analytics(request):
    # bw = 
    return render(request,"Workforce_analytics.html")

def contact(request):
    return render(request,"contact.html")

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")