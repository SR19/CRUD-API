from rest_framework import serializers
from ClientAdmin.models import admin,client

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=admin 
        fields=('AdminID','AdminName')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=client 
        fields=('ClientID','ClientName','ClientDOJ','ClientDept','ClientName')