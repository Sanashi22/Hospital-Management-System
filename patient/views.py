from django.shortcuts import render,redirect
from .models import Patient
from .forms import Patientcreateupdateform

# Create your views here.

def aboutus(request):
    return render(request, 'aboutus.html')

def homepage(request):
    return render(request, 'homepage.html')

def contactus(request):
    return render(request, 'contactus.html')


def create_patient(request):
    if request.method=='POST':
        form=Patientcreateupdateform(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()

            return redirect('/')
    
    form= Patientcreateupdateform()
    return render(request,'add-patient.html',{'form':form, 'title':'Add'})

def patient_list(request):
    patient=Patient.objects.all()
    return render(request,'patientlist.html',{'patients':patient})

def patient_delete(request,id):
    Patient.objects.get(id=id).delete()
    return redirect('patient:patient-list')

def update_patient(request,id):
    patient=Patient.objects.get(id=id)
    if request.method=='POST':
        form=Patientcreateupdateform(request.POST,instance=patient)
        if form.is_valid():
           form.save()

           return redirect('patient:patient-list')
   
    form= Patientcreateupdateform(instance=patient)
    return render(request,'add-patient.html',{'form':form, 'title':'Update'})


