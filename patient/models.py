from django.db import models
from doctor.models import Doctor

# Create your models here.

GENDER= ( 
    ('male','Male'),('female','Female')
)

class Patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField ()
    diagnnosis=models.TextField()
    email= models.CharField(max_length=100)
    gender= models.CharField(max_length=10, choices=GENDER)
    doctor= models.ForeignKey(Doctor,on_delete=models.SET_NULL, null= True)

    def __str__(self) -> str:
        return f"{self.name} - Patient created"


    