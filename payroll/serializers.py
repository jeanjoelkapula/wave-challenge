from rest_framework import serializers
from .models import TimeReport

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeReport
        fields = '__all__'

class FileSerializer(serializers.Serializer):
    file = serializers.FileField()