# Generated by Django 5.1 on 2024-09-19 05:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0002_doctorregister_delete_doctor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorregister',
            name='specialization',
        ),
        migrations.AddField(
            model_name='doctorregister',
            name='department',
            field=models.CharField(choices=[('Department', 'Department'), ('Cardiologist', 'Cardiologist'), ('Dermatologist', 'Dermatologist'), ('Emergency Medicine Specialist', 'Emergency Medicine Specialist'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologist', 'Anesthesiologist'), ('General', 'General'), ('Pediatrician', 'Pediatrician')], default='Department', max_length=50),
        ),
        migrations.AlterField(
            model_name='doctorregister',
            name='gender',
            field=models.CharField(blank=True, choices=[('', 'Gender'), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
        migrations.CreateModel(
            name='PatientRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('profile_pic', models.ImageField(null=True, upload_to='profile_pic/doctorprofilePic/')),
                ('address', models.CharField(max_length=100)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('', 'Gender'), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]