# serializers.py

from rest_framework import serializers
from .models import Employee,Job, Breakdown


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class BreakdownSerializer(serializers.ModelSerializer):

    class Meta:
        model = Breakdown
        fields = '__all__'
