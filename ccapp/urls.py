from django.contrib.auth.views import LoginView
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views 


urlpatterns = [
    path('', views.index),
    path('adminclick/', views.adminclickview, name="adminclick"),
    path('admin-dashboard/', views.admin_dashboardview, name="admin-dashboard"),

    path('doctorclick/', views.doctorclickview, name="doctorclick"),
    path('doctorregister/', views.doctorregisterview, name="doctorregister"),
    path('doctorlogin/', views.doctor_login_view, name="doctorlogin"),
    path('admindoctor-dashboard/', views.admindoctor_dashboardview, name="admindoctor-dashboard"),
    path('admindoctoradd-dashboard/', views.admindoctoradd_dashboardview, name="admindoctoradd-dashboard"),
    path('admindoctorview-dashboard/', views.admindoctorview_dashboardview, name="admindoctorview-dashboard"),
    path('admindoctorrequest-dashboard/', views.admindoctorrequest_dashboardview, name="admindoctorrequest-dashboard"),
    path('approve-doctor/<int:pk>', views.approve_doctor_view,name='approve-doctor'),
    path('reject-doctor/<int:pk>', views.reject_doctor_view,name='reject-doctor'),
    path('doctor-dashboard/', views.doctor_dashboardview, name="doctor-dashboard"),

    path('patientclick/', views.patientclickview, name="patientclick"),
    path('patientregister/', views.patientregisterview, name="patientregister"),
    path('patientlogin/', views.patient_login_view, name="patientlogin"),
    path('adminpatient-dashboard/', views.adminpatient_dashboardview, name="adminpatient-dashboard"),
    path('adminpatientadd-dashboard/', views.adminpatientadd_dashboardview, name="adminpatientadd-dashboard"),
    path('adminpatientview-dashboard/', views.adminpatientview_dashboardview, name="adminpatientview-dashboard"),
    path('adminpatientrequest-dashboard/', views.adminpatientrequest_dashboardview, name="adminpatientrequest-dashboard"),
    path('approve-patient/<int:pk>', views.approve_patient_view,name='approve-patient'),
    path('reject-patient/<int:pk>', views.reject_patient_view,name='reject-patient'),
    path('patient-dashboard/', views.patient_dashboardview, name="patient-dashboard"),


    path('pharmacyclick/', views.pharmacyclickview, name="pharmacyclick"),
    path('adminpharmacy-dashboard/', views.adminpharmacy_dashboardview, name="adminpharmacy-dashboard"),
   
    path('doctor_wait_for_approval/', views.doctor_wait_for_approvalview, name="doctor_wait_for_approval"),
    path('patient_wait_for_approval/', views.patient_wait_for_approvalview, name="patient_wait_for_approval"),

    path('patient-booking/', views.patient_bookingview, name="patient-booking"),
    path('patient-consultation/', views.patient_consultationview, name="patient-consultation"),
    path('patient-prescription/', views.patient_prescriptionview, name="patient-prescription"),
    path('patient-purchasing/', views.patient_purchasingview, name="patient-purchasing"),
    path('book-appointment/', views.book_appointmentview, name="book-appointment"),
    path('book-appointment/view-appointment/', views.view_appointmentview, name="view-appointment"),


    path('doctor-booking/', views.doctor_bookingview, name="doctor-booking"),
    path('doctor-consultation/', views.doctor_consultationview, name="doctor-consultation"),
    path('doctor-prescription/', views.doctor_prescriptionview, name="doctor-prescription"),

    path('logout/',views.logoutview, name='logout'),

    path('admin-booking/', views.admin_booking_view, name="admin-booking"),
    path('admin-add-booking/admin-view-booking/', views.admin_view_booking_view, name="admin-view-booking"),
    path('admin-add-booking/', views.admin_add_booking_view, name="admin-add-booking"),
    path('admin-approve-booking/', views.admin_approve_booking_view, name="admin-approve-booking"),
    path('approve-booking/<int:pk>', views.approve_booking_view, name="approve-booking"),
    path('reject-booking/<int:pk>', views.reject_booking_view, name="reject-booking"),

    path('ayurveda-doctors/', views.ayurveda_doctors_view, name="ayurveda-doctors"),
    path('homeopathy-doctors/', views.homeopathy_doctors_view, name="homeopathy-doctors"),
    path('ent-doctors/', views.ent_doctors_view, name="ent-doctors"),
    path('physiotherapy-doctors/', views.physiotherapy_doctors_view, name="physiotherapydoctors"),
    path('phsycology-doctors/', views.phsycology_doctors_view, name="phsycology-doctors"),
    path('general-doctors/', views.general_doctors_view, name="general-doctors"),


]
