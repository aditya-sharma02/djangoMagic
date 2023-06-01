from rest_framework import serializers
from api.models import Company



class CompanySerializers(serializers.HyperlinkedModelSerializer):
    # serializers.HyperlinkedModelSerializer provide functionality of meta class
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"