from django.db import models
from sqlalchemy import null
from django.utils import timezone

# Create your models here.
class JobGroup(models.Model):
    id = models.CharField(max_length=1, null=False, blank=False, primary_key=True)
    hourlyRate = models.FloatField(null=False, blank=False)

    def __str__(self):
        return f"{self.id} - {self.hourlyRate}"

class Employee(models.Model):
    employeeId = models.IntegerField(primary_key=True)
    jobGroup = models.ForeignKey(JobGroup, null=False, blank=False, on_delete=models.DO_NOTHING, related_name="groupEmployees")

    def __str__(self):
            return f"{self.employeeId} {self.jobGroup}"

class TimeReport(models.Model):
    id = models.IntegerField(null=False, blank=False, primary_key=True)
    date = models.DateField(auto_now_add=True)

class TimeReportLine(models.Model):
    report = models.ForeignKey(TimeReport,null=False, blank=False, on_delete=models.CASCADE, related_name="reportLines")
    date = models.DateField(null=False)
    hoursWorked = models.FloatField(null=False)
    employee = models.ForeignKey(Employee,null=False, blank=False, on_delete=models.DO_NOTHING, related_name="timeReports")

    def __str__(self):
        return f"{self.report.id} - {self.date} - {self.hoursWorked} - {self.employee.employeeId}"