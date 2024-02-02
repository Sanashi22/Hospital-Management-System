from django.forms import ModelForm
from .models import Doctor

class Doctorcreateupdateform(ModelForm):
    class Meta:
        model=Doctor
        fields="__all__"

