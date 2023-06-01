from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company
from api.serializers import CompanySerializers
from api.models import Employee
from api.serializers import EmployeeSerializers
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

# defining the route /companies/{company_id}/employees/
# the word "employees" used to define the function must be same as the "employees " used in the route
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company = company)
            emps_serializers = EmployeeSerializers(emps,many=True,context={'request':request})
            return Response(emps_serializers.data)
        except Exception as e:
            print(e)
            return Response({'message':"Company not Exits"})

    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers