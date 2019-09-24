from rest_framework_mongoengine import viewsets 
from employee.models import Employee
from employee.serializers import EmployeeSerializer


# Create your views here.

# ModelViewSet, to operate all the  CRUD operations, and can be access all the time
# If viewset is there then we can use routers and it generate the urls for all CRUD operations
class EmployeeView(viewsets.ModelViewSet):
    lookup_field = 'empId'
    queryset = Employee.objects.all()    
    serializer_class = EmployeeSerializer
