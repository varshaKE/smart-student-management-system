# Generated by Django 3.2.25 on 2025-03-30 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smart_student_app', '0003_rename_total_weekdays_attendance_weekday_count'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attendance',
        ),
    ]
