# Generated by Django 5.1 on 2024-10-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0007_remove_patientregister_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('doctorId', models.PositiveIntegerField(null=True)),
                ('patientName', models.CharField(max_length=40, null=True)),
                ('doctorName', models.CharField(max_length=40, null=True)),
                ('appointmentDate', models.DateField(auto_now=True)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
