from rest_framework import generics
from rest_framework.response import Response

from payroll.models import Employee
from .serializers import *
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.views import APIView
import csv
from io import StringIO
from datetime import datetime

# Create your views here.
class ReportsList(generics.ListCreateAPIView):
    serializer_class = ReportSerializer

    def get(self, request):


        return Response({'request': 'GET'})

class FileUploadView(APIView):
    parser_classes = [MultiPartParser]
    serializer_class = FileSerializer

    def put(self, request, format=None):
        file_obj = request.data['file']

        #file name format time-report-42.csv
        #extract report id
        id = int(file_obj.split('.')[0].split('-')[2])

        #check report id
        try:
            report = TimeReport.objects.get(id=id)

            return Response({'message': 'this report has already been submitted. You may submit a report only once'})
            
        except TimeReport.DoesNotExist:
            csvf = StringIO(file_obj.read().decode())
            csvreader = csv.reader(csvf)
            header = next(csvreader)
            for row in csvreader:
                date = datetime.strptime(row[0], '%d/%m/%Y').date()
                hours = float(row[1])
                employeeid = int(row[2])
                report = TimeReport(id=id, date=date, hoursWorked=hours, employee=employeeid)
                report.save()

        return Response({'message': 'the report was successfully submitted'})