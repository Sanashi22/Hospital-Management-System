from django.db import models
from doctor.models import Doctor
from patient.models import Patient
# Create your models here.

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    comment = models.TextField(null=True)
    created=models.DateTimeField(auto_now_add= True)
    updated=models.DateTimeField(auto_now= True)

    def __str__(self) -> str:
        return f"{self.doctor.name} - {self.patient.name} - appointment created"