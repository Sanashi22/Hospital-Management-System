from django.shortcuts import render
from .models import Doctor

# Create your views here.
def homepage(request):
    doctors= Doctor.objects.all()
    context={
        "doctors":doctors

    }

    return render(request,"doctorlist.html",context=context)