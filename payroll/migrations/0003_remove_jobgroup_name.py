# Generated by Django 4.0.2 on 2022-02-17 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0002_alter_employee_employeeid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobgroup',
            name='name',
        ),
    ]
