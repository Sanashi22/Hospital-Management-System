from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Appointment

class LoginForm(forms.Form):
    username=forms.CharField (max_length=100, label= "username" )
    password=forms.CharField (max_length=100, label= "password", widget=forms.PasswordInput())

class Signupform(UserCreationForm):
    class Meta:
        model= User
        fields= ('username','first_name','last_name','email','password1','password2')

class Appointmentform(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=('doctor','patient','appointment_date','comment')
    
        widgets={
        'appointment_date':forms.TextInput(attrs={'type':'datetime-local'})
        }


class Appointmentcreateupdateform(forms.ModelForm):
    class Meta:
        model=Appointment
        fields="__all__"
