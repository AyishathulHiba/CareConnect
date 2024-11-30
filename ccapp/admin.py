from django.contrib import admin
from . models import DoctorRegister,PatientRegister,Appointment,Department
admin.site.register(DoctorRegister)
admin.site.register(PatientRegister)
admin.site.register(Appointment)
admin.site.register(Department)


