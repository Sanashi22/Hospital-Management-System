from django.urls import path 
from .views import homepage
app_name="doctor"
urlpatterns = [
    path('', homepage,name='homepage')
]
