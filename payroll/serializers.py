from rest_framework import serializers
from .models import *
from calendar import monthrange
from django.db.models import F
from django.db.models import Sum

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeReport
        fields = '__all__'
        depth = 1

    def get_payroll(self):
        data = {'payrollReport':{
                'employeeReports': []
            }
        }
        
        #reported years
        reported_years = TimeReportLine.objects.values(year=F('date__year')).distinct().order_by('year')

        for year_dict in reported_years:
            year = year_dict['year']
            
            #reported months
            reported_months = TimeReportLine.objects.filter(date__year=year).values(month=F('date__month')).distinct().order_by('month')

            #employee pay for reported months in current year
            for employee in Employee.objects.order_by('employeeId').all():

                for month_dict in reported_months:
                    month = month_dict['month']

                    #month total days
                    num_days = monthrange(year, month)[1]

                    #first half of the month pay
                    first_period_hours = employee.timeReports.filter(date__year=year, date__month=month, date__day__lte=15).aggregate(Sum('hoursWorked'))['hoursWorked__sum']
                    if first_period_hours is not None:
                        first_period_pay = (employee.jobGroup.hourlyRate * first_period_hours)
                        if first_period_pay > 0:
                            data['payrollReport']['employeeReports'].append({
                                'employeeId': employee.employeeId,
                                'payPeriod':{
                                'startPeriod': f"{year}-{month}-1",
                                'endPeriod': f"${year}-{month}-15"
                                },
                                'amountPaid': "${:.2f}".format(first_period_pay)
                            })
                            
                    #second half of the month pay
                    second_period_hours = employee.timeReports.filter(date__year=year, date__month=month, date__day__gte=16).aggregate(Sum('hoursWorked'))['hoursWorked__sum']
                    if second_period_hours is not None:
                        second_period_pay = (employee.jobGroup.hourlyRate * second_period_hours)

                        if second_period_pay > 0:
                            data['payrollReport']['employeeReports'].append({
                                'employeeId': employee.employeeId,
                                'payPeriod': {
                                    'startPeriod': f"{year}-{month}-16",
                                    'endPeriod': f"{year}-{month}-{num_days}"
                                },
                                'amountPaid': "{:.2f}".format(second_period_pay)
                            })
        return data
        
class FileSerializer(serializers.Serializer):
    file = serializers.FileField()