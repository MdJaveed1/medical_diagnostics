# Generated by Django 5.0.1 on 2024-12-07 02:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
        ('doctor', '0001_initial'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicalrecord',
            old_name='insights',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='medicalrecord',
            name='date_uploaded',
        ),
        migrations.RemoveField(
            model_name='medicalrecord',
            name='medicines',
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='appointment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appointments.appointment'),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctorprofile'),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='record_file',
            field=models.FileField(upload_to='medical_records/'),
        ),
    ]