from django.shortcuts import render

# Create your views here.

def aboutus(request):
    return render(request, 'aboutus.html')

def homepage(request):
    return render(request, 'homepage.html')

def contactus(request):
    return render(request, 'contactus.html')