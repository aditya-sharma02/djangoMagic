from rest_framework import serializers
from api.models import Company



class CompanySerializers(serializers.HyperlinkedModelSerializer):
    # serializers.HyperlinkedModelSerializer provide functionality of meta class
    class Meta:
        model = Company
        feilds = "__all__"