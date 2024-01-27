from django.urls import path
from .views import aboutus, homepage, contactus
app_name= 'patient'

urlpatterns = [
    path('aboutus',aboutus,name='aboutus'),
     path('',homepage,name='homepage'),
     path('contactus',contactus, name='contactus')

]
