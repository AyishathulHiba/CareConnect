from django import forms
from .models import DoctorRegister
from django.contrib.auth.models import User
from .models import PatientRegister
from . import models

class DoctorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        
class DoctorRegisterForm(forms.ModelForm):
    class Meta:
        model = DoctorRegister
        fields = ['mobile', 'email','department','profile_pic','medical_license']
        
class PatientForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

        
class PatientRegisterForm(forms.ModelForm):
    class Meta:
        model = PatientRegister
        fields = ['mobile', 'email', 'address', 'dob']


class AppointmentForm(forms.ModelForm):
    doctorId=forms. ModelChoiceField(queryset=models.DoctorRegister. objects.all() .filter(status=True), empty_label="Doctor Name and Department", to_field_name="user_id")
    patientId=forms.ModelChoiceField(queryset=models.PatientRegister.objects.all().filter(status=True), empty_label="Patient Name and Symptoms", to_field_name="user_id") 
    class Meta:
        model=models.Appointment 
        fields=['description', 'status']
