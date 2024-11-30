from django.db import models
from django.contrib.auth.models import User

departments = [
    ("Department", "Department"), 
    ("Cardiologist", "Cardiologist"),
    ("Dermatologist", "Dermatologist"),
    ("Emergency Medicine Specialist", "Emergency Medicine Specialist"),
    ("Allergists/Immunologists", "Allergists/Immunologists"),
    ("Anesthesiologist", "Anesthesiologist"),
    ("General", "General"),
    ("Pediatrician", "Pediatrician")  
]


class DoctorRegister(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10, null=False)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to="profile_pic/doctorprofilePic/", null=True)
    medical_license = models.FileField(upload_to='licenses/', null=True, blank=True)
    department = models.CharField(max_length=50, choices=departments, default="Department")
    status = models.BooleanField(default=False)
    
    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    # Corrected __str__ method
    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.department)
     
class PatientRegister(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        mobile = models.CharField(max_length=10, null=False)
        email = models.EmailField()
        address = models.CharField(max_length=100)
        dob = models.DateField(null=True, blank=True) 
        status = models.BooleanField(default=False) 
        

class Appointment(models.Model):
        patientId=models.PositiveIntegerField(null=True)
        doctorId=models.PositiveIntegerField(null=True)
        patientName=models.CharField(max_length=40, null=True)
        doctorName=models.CharField(max_length=40, null=True)
        appointmentDate=models.DateField(auto_now=True)
        description=models.TextField(max_length=500)
        status=models.BooleanField(default=False)

class Department(models.Model):
     department=models.CharField(max_length=50)
     description=models.TextField(null=True,blank=True)

     def __str__(self):
          return f"Derpartment {self.department}"



