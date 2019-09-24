from employee.models import Employee
from rest_framework_mongoengine import serializers
# serializers here are library from mongo engine

class EmployeeSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Employee
        fields = "__all__"