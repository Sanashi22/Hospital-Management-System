from django.shortcuts import render,redirect
from .forms import LoginForm, Signupform, Appointmentform
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Appointment



# Create your views here.

def user_login(request):
    forms=LoginForm()
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]  
            password=form.cleaned_data["password"]
            user=authenticate(request, username=username, password=password)
            if user: 
                login(request, user)
                return redirect("adminstrator:dashboard")

    context= {"form": forms }
    return render(request,"login.html", context)


def signup(request):
    forms=Signupform()
    if request.method=="POST":
        form=Signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")

    context= {"form": forms }
    return render(request,"signup.html",context)
@login_required()
def schedule_appointment(request):
    forms=Appointmentform()
    if request.method=="POST":
        form=Appointmentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        
    return render(request,"appointment.html",{"form": forms})


def dashboard(request):
    appointment=Appointment.objects.all()
    return render(request, "dashboard.html",{'appointments':appointment})

def logout_user(request):
    logout(request)
    return redirect('/')



