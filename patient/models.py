from django.db import models

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
    

    def __str__(self) -> str:
        return f"{self.name} - Patient created"


