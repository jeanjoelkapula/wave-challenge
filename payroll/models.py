from django.db import models
from sqlalchemy import null

# Create your models here.
class JobGroup(models.Model):
    id = models.CharField(max_length=1, null=False, blank=False)
    name = models.TextField(max_length=65, null=False, blank=False)
    hourlyRate = models.FloatField(null=False, blank=False)

class Employee(models.Model):
    employeeId = models.AutoField(primary_key=True)
    jobGroup = models.ForeignKey(JobGroup, null=False, blank=False, related_name="groupEmployees")

class TimeReport(models.Model):
    id = models.IntegerField(null=False, blank=False, primary_key=True)
    date = models.DateField(auto_now_add=True)
    hoursWorked = models.FloatField(null=False)
    employee = models.ForeignKey(Employee,null=False, blank=False, related_name="timeReports")
