from .models import *

def insert_records():
    groups = JobGroup.objects.all().count()
    if groups == 0:
        data = [{'id': 'A', 'rate': 20}, {'id': 'B','rate': 30}]
        for group in data:
            JobGroup(id=group['id'], hourlyRate=group['rate']).save()

    employees = Employee.objects.all().count()
    if employees == 0:
        data = [
            {
                'id': 1,
                'group': 'A'
            },
             {
                'id': 2,
                'group': 'B'
            },
             {
                'id': 3,
                'group': 'A'
            },
             {
                'id': 4,
                'group': 'B'
            },
        ]

        for emp in data:
            group = JobGroup.objects.get(id=emp['group'])
            Employee(employeeId=emp['id'], jobGroup=group).save()