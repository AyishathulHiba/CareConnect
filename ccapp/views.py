from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import Group
from .forms import DoctorForm, DoctorRegisterForm, PatientForm, PatientRegisterForm,AppointmentForm
from django.contrib.auth.models import User
from  . import models
from . import forms


# Index View
def index(request):
    department=models.Department.objects.all()
    return render(request, "index.html" , {"context":department})


# Admin Click View
def adminclickview(request):
    return render(request, "adminclick.html")


# Doctor Click View
def doctorclickview(request):
    return render(request, 'doctorclick.html')


# Patient Click View
def patientclickview(request):
    return render(request, "patientclick.html")


# Pharmacy Click View
def pharmacyclickview(request):
    return render(request, "pharmacyclick.html")


# Doctor Register View
def doctorregisterview(request):
    userform = DoctorForm()
    doctorform = DoctorRegisterForm()
    mydict = {'userform': userform, 'doctorform': doctorform}
    
    if request.method == 'POST':
        userform = DoctorForm(request.POST)
        doctorform = DoctorRegisterForm(request.POST, request.FILES)
        
        if userform.is_valid() and doctorform.is_valid():
            user = userform.save(commit=False)
            user.set_password(user.password)
            user.save()
            doctor = doctorform.save(commit=False)
            doctor.user = user
            doctor.save()
            my_doctor_group, _ = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group.user_set.add(user)
        return HttpResponseRedirect(reverse('doctorlogin'))
    
    return render(request, "doctorregister.html", context=mydict)

# Custom Login View for Admins
def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None and is_admin(user):
            login(request, user)
            return redirect('admin-dashboard')
        else:
            return render(request, 'adminlogin.html', {'error': 'Invalid credentials or not an admin account.'})
    
    return render(request, 'adminlogin.html')

# Patient Register View
def patientregisterview(request):
    userform = PatientForm()
    patientform = PatientRegisterForm()
    mydict = {'userform': userform, 'patientform': patientform}
    
    if request.method == 'POST':
        userform = PatientForm(request.POST)
        patientform = PatientRegisterForm(request.POST, request.FILES)
        
        if userform.is_valid() and patientform.is_valid():
            user = userform.save(commit=False)
            user.set_password(user.password)
            user.save()
            patient = patientform.save(commit=False)
            patient.user = user
            patient.save()
            my_patient_group, _ = Group.objects.get_or_create(name='PATIENT')
            my_patient_group.user_set.add(user)
            return HttpResponseRedirect(reverse('patientlogin'))
    
    return render(request, "patientregister.html", context=mydict)


# Custom Login View for Doctors
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

import logging

logger = logging.getLogger(__name__)

def doctor_login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            logger.info("User logged in: %s", username)
            return redirect('doctor_wait_for_approval')
        else:
            logger.warning("Failed login attempt for username: %s", username)
            messages.error(request, "Invalid username or password.")
            return render(request, 'doctorlogin.html')

    return render(request, 'doctorlogin.html')




# Custom Login View for Patients
def patient_login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('patient_wait_for_approval')  # Redirect to the approval page
        else:
            error = "Invalid username or password."
            return render(request, 'patientlogin.html', {'error': error})

    return render(request, 'patientlogin.html')



# Helper Functions to Check User Groups
def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()

def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()

def admin_dashboardview(request):
    return render(request, "admin-dashboard.html")

# Doctor Dashboard View
def admindoctor_dashboardview(request):
    return render(request, "admindoctor-dashboard.html")

# Patient Dashboard View
def adminpatient_dashboardview(request):
    return render(request, "adminpatient-dashboard.html")

def adminpharmacy_dashboardview(request):
    return render(request, "adminpharmacy-dashboard.html")

def admindoctoradd_dashboardview(request):
    userform = DoctorForm()
    doctorform = DoctorRegisterForm()
    mydict = {'userform': userform, 'doctorform': doctorform}
    
    if request.method == 'POST':
        userform = DoctorForm(request.POST)
        doctorform = DoctorRegisterForm(request.POST, request.FILES)
        
        if userform.is_valid() and doctorform.is_valid():
            user = userform.save(commit=False)
            user.set_password(user.password)
            user.save()
            doctor = doctorform.save(commit=False)
            doctor.user = user
            doctor.save()
            my_doctor_group, _ = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group.user_set.add(user)
        return HttpResponseRedirect(reverse('admindoctorview-dashboard'))
    
    return render(request, "doctorregister.html", context=mydict)



def admindoctorview_dashboardview(request):
    # Fetch doctors with status True (approved)
    doctors = models.DoctorRegister.objects.all()
    print(doctors)
    return render(request, "admindoctorview-dashboard.html", {"doctors": doctors})


def admindoctorrequest_dashboardview(request):
    doctors=models.DoctorRegister.objects.all().filter(status=False)
    return render(request,'admindoctorrequest-dashboard.html',{'doctors':doctors})

def approve_doctor_view(request,pk):
    doctors=models.DoctorRegister.objects.get(id=pk)
    doctors.status=True
    doctors.save()
    return redirect(reverse('admindoctorrequest-dashboard'))

def reject_doctor_view(request,pk):
    doctors=models.DoctorRegister.objects.get(id=pk)
    user=models.User.objects.get(id=doctors.user_id)
    user.delete()
    doctors.delete()
    return redirect('admindoctorrequest-dashboard')

def adminpatientadd_dashboardview(request):
    userform = PatientForm()
    patientform = PatientRegisterForm()
    mydict = {'userform': userform, 'patientform': patientform}

    
    if request.method == 'POST':
        userform = PatientForm(request.POST)
        patientform = PatientRegisterForm(request.POST, request.FILES)
        
        if userform.is_valid() and patientform.is_valid():
            user = userform.save(commit=False)
            user.set_password(user.password)
            user.save()
            patient = patientform.save(commit=False)
            patient.user = user
            patient.save()
            my_patient_group, _ = Group.objects.get_or_create(name='PATIENT')
            my_patient_group.user_set.add(user)
            return HttpResponseRedirect(reverse('adminpatientview-dashboard'))
    
    return render(request, "patientregister.html", context=mydict)
    

def adminpatientview_dashboardview(request):
    patients = models.PatientRegister.objects.all()
    print(patients)
    return render(request, "adminpatientview-dashboard.html", {"patients": patients})

def adminpatientrequest_dashboardview(request):
    patients=models.PatientRegister.objects.all().filter(status=False)
    return render(request,'adminpatientrequest-dashboard.html',{'patients':patients})

def approve_patient_view(request,pk):
    patients=models.PatientRegister.objects.get(id=pk)
    patients.status=True
    patients.save()
    return redirect(reverse('adminpatientrequest-dashboard'))

def reject_patient_view(request,pk):
    patients=models.PatientRegister.objects.get(id=pk)
    user=models.User.objects.get(id=patients.user_id)
    user.delete()
    patients.delete()
    return redirect('adminpatientrequest-dashboard')

def doctor_wait_for_approvalview(request):
    accountapproval = models.DoctorRegister.objects.all().filter(user_id=request.user.id, status=True)
    if accountapproval:
            return redirect('doctor-dashboard')
    else:
            return render(request, "doctor_wait_for_approval.html")
def patient_wait_for_approvalview(request):
    accountapproval = models.PatientRegister.objects.all().filter(user_id=request.user.id, status=True)
    if accountapproval:
            return redirect('patient-dashboard')
    else:
        return render(request, "patient_wait_for_approval.html")

def logoutview(request):
    return render(request, "logout.html")

def doctor_dashboardview(request):
    return render(request, "doctor-dashboard.html")
def patient_dashboardview(request):
    return render(request, "patient-dashboard.html")

def patient_bookingview(request):
    return render(request, "patient-booking.html")
def patient_consultationview(request):
    return render(request, "patient-consultation.html")
def patient_prescriptionview(request):
    return render(request, "patient-prescription.html")
def patient_purchasingview(request):
    return render(request, "patient-purchasing.html")


def book_appointmentview(request):
    appointmentform=forms.AppointmentForm()
    patient=models.PatientRegister.objects.get(user_id=request.user.id)
    message=None
    mydict={'appointmentform': appointmentform, 'patient':patient, 'message': message} 
    if request.method== 'POST' :
        appointmentform=forms.AppointmentForm(request.POST)
        print (request.POST)
        print (request.user.id)
        if appointmentform.is_valid():
            print (request. POST.get('doctorId')) 
            desc=request. POST. get ('description')
            doctor=models. DoctorRegister.objects.get(user_id=request.POST.get('doctorId'))
            appointment=appointmentform.save(commit=False)
            appointment.doctorId=request.POST.get('doctorId') 
            appointment.patientId=request.user.id 
            appointment.doctorName=models. User .objects.get (id=request. POST.get('doctorId')).first_name 
            appointment.patientName=request.user.first_name
            appointment.status=False
            appointment.save()
        else:
            print (appointmentform.errors)
        return HttpResponseRedirect( 'view-appointment' )
    return render(request, "book-appointment.html",context=mydict)

def view_appointmentview(request):
    appointments = models.Appointment.objects.filter(patientId=request.user.id)
    return render(request, "view-appointment.html",{"appointments": appointments})

def doctor_bookingview(request):
    return render(request, "doctor-booking.html")
def doctor_consultationview(request):
    return render(request, "doctor-consultation.html")
def doctor_prescriptionview(request):
    return render(request, "doctor-prescription.html")

def admin_booking_view(request):
    return render (request, 'admin_booking.html')
def admin_view_booking_view(request):
    appointments = models.Appointment.objects.all()
    print(appointments)
    return render (request, 'admin_view_booking.html', {"appointments": appointments})

def admin_add_booking_view(request):
    appointmentForm=forms.AppointmentForm()
    mydict={'appointmentForm':appointmentForm,}
    if request.method=='POST':
        appointmentForm=forms.AppointmentForm(request.POST)
        if appointmentForm.is_valid():
            appointment=appointmentForm.save(commit=False)
            appointment.doctorId=request.POST.get('doctorId')
            appointment.patientId=request.POST.get('patientId')
            appointment.doctorName=models.User.objects.get(id=request.POST.get('doctorId')).first_name
            appointment.patientName=models.User.objects.get(id=request.POST.get('patientId')).first_name
            appointment.status-True
            appointment.save()
            return HttpResponseRedirect('admin-view-booking')
    return render (request, 'admin_add_booking.html',context=mydict)

def admin_approve_booking_view(request):
    appointments=models.Appointment.objects.all().filter(status=False)
    return render (request, 'admin_approve_booking.html',{'appointments':appointments})

def approve_booking_view(request,pk):
    appointment=models.Appointment.objects.get(id=pk)
    appointment.status=True
    appointment.save()
    return redirect(reverse('admin-approve-booking'))

def reject_booking_view(request,pk):
    appointment=models.Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect ('admin-approve-booking')

def ayurveda_doctors_view(request):
    return render (request, 'ayurveda_doctors.html')
def homeopathy_doctors_view(request):
    return render (request, 'homeopathy_doctors.html')
def ent_doctors_view(request):
    return render (request, 'ent_doctors.html')
def general_doctors_view(request):
    return render (request, 'general_doctors.html')
def physiotherapy_doctors_view(request):
    return render (request, 'physiotherapy_doctors.html')
def phsycology_doctors_view(request):
    return render (request, 'phsycology_doctors.html')
