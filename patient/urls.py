from django.urls import path
from .views import aboutus, homepage, contactus, create_patient,patient_list,patient_delete, update_patient
app_name= 'patient'

urlpatterns = [
    path('aboutus',aboutus,name='aboutus'),
     path('',homepage,name='homepage'),
     path('contactus',contactus, name='contactus'),
    path('create',create_patient,name='create-patient'),
    path('patient-list',patient_list,name='patient-list'),
    path('patient-delete/<int:id>',patient_delete,name='patient-delete'),
    path('patient-update/<int:id>',update_patient,name='patient-update')

]
