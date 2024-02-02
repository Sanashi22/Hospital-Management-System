from django.shortcuts import render,redirect
from .models import Doctor
from .forms import Doctorcreateupdateform

# Create your views here.
def homepage(request):
    doctors= Doctor.objects.all()
    context={
        "doctors":doctors

    }

    return render(request,"doctorlist.html",context=context)

def create_doctor(request):
    if request.method=='POST':
        form=Doctorcreateupdateform(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()

            return redirect('/')
    
    form=Doctorcreateupdateform()
    return render(request,'add-doctor.html',{'form':form})

def doctor_list(request):
    doctor=Doctor.objects.all()
    return render(request,'doctorlist.html',{'doctors':doctor})
    
def doctor_delete(request,id):
    Doctor.objects.get(id=id).delete()
    return redirect('doctor:doctor-list')

def update_doctor(request,id):
    doctor=Doctor.objects.get(id=id)
    if request.method=='POST':
        form=Doctorcreateupdateform(request.POST,instance=doctor)
        if form.is_valid():
           form.save()

           return redirect('doctor:doctor-list')
   
    form= Doctorcreateupdateform(instance=doctor)
    return render(request,'add-doctor.html',{'form':form, 'title':'Update'})
