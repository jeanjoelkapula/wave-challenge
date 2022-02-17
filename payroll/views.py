from rest_framework import generics
from rest_framework.response import Response

from payroll.models import *
from .serializers import *
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.views import APIView
import csv
from io import StringIO
from datetime import datetime


# Create your views here.
class ReportsList(generics.ListAPIView):
    queryset = TimeReport.objects.order_by('id', 'date').all()
    serializer_class = ReportSerializer

    def get(self, request):
        queryset = Employee.objects.order_by('employeeId').all()
        data = ReportSerializer().get_payroll()

        return Response(data)

class FileUploadView(APIView):
    parser_classes = [MultiPartParser]
    serializer_class = FileSerializer

    def put(self, request, format=None):
        file_obj = request.data['file']

        #file name format time-report-42.csv
        #extract report id
        id = int(file_obj.name.split('.')[0].split('-')[2])

        #check report id
        try:
            report = TimeReport.objects.get(id=id)

            return Response({'message': 'this report has already been submitted. You may submit a report only once'})

        except TimeReport.DoesNotExist:
            csvf = StringIO(file_obj.read().decode())
            csvreader = csv.reader(csvf)
            header = next(csvreader)
            
            report = TimeReport(id=id)
            report.save()

            for row in csvreader:
                date = datetime.strptime(row[0], '%d/%m/%Y').date()
                hours = float(row[1])
                employee = Employee.objects.get(employeeId= int(row[2]))
                entry = TimeReportLine(report=report, date=date, hoursWorked=hours, employee=employee)
                entry.save()

        return Response({'message': 'the report was successfully submitted'})