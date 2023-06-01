from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company
from api.serializers import CompanySerializers
from api.models import Employee
from api.serializers import EmployeeSerializers
from rest_framework.decorators import action


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

# defining the route /companies/{company_id}/employees/
# the word "employees" used to define the function must be same as the "employees " used in the route
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        pass

    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers