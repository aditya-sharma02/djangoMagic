from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company
from api.serializers import CompanySerializers
from companyapi.api.models import Employee
from companyapi.api.serializers import EmployeeSerializers

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers