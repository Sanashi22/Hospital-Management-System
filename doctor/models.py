from django.db import models
from patient.models import Patient

# Create your models here.

GENDER= ( 
    ('male','Male'),('female','Female')
)
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    dea_number= models.CharField(max_length=50)
    email= models.CharField(max_length=100)
    gender= models.CharField(max_length=10, choices=GENDER)
    profile_picture= models.ImageField(upload_to="Doctor")

    def __str__(self) -> str:
        return f"{self.name} - doctor created"
    
