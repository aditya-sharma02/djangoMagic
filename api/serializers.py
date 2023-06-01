from rest_framework import serializers
from api.models import Company
from companyapi.api.models import Employee



class CompanySerializers(serializers.HyperlinkedModelSerializer):
    # serializers.HyperlinkedModelSerializer provide functionality of meta class
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"