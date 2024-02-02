from django.urls import path 
from .views import homepage,create_doctor,update_doctor,doctor_delete,doctor_list
app_name="doctor"
urlpatterns = [
    path('', homepage,name='homepage'),
    path('create',create_doctor,name='create-doctor'),
    path('doctor-delete/<int:id>',doctor_delete,name='doctor-delete'),
    path('doctor-update/<int:id>',update_doctor,name='doctor-update'),
    path('doctor-list',doctor_list,name='doctor-list'),

]
