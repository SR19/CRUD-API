

# Create your views here.

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ClientAdmin.models import admin,client
from ClientAdmin.serializers import AdminSerializer,ClientSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def adminApi(request,id=0):
    if request.method=='GET':
        admin = admin.objects.all()
        admin_serializer=adminSerializer(admin,many=True)
        return JsonResponse(admin_serializer.data,safe=False)
    elif request.method=='POST':
        admin_data=JSONParser().parse(request)
        admin_serializer=adminerializer(data=admin_data)
        if admin_serializer.is_valid():
            admin_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        admin_data=JSONParser().parse(request)
        admin=admin.objects.get(AdminID=admin_data['AdminID'])
        admin_serializer=adminSerializer(admin,data=admin_data)
        if admin_serializer.is_valid():
            admin_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        admin=admin.objects.get(AdminID=id)
        admin.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def ClientApi(request,id=0):
    if request.method=='GET':
        client = client.objects.all()
        client_serializer=clienterializer(client,many=True)
        return JsonResponse(client_serializer.data,safe=False)
    elif request.method=='POST':
        client_data=JSONParser().parse(request)
        client_serializer=clientSerializer(data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        client_data=JSONParser().parse(request)
        client=client.objects.get(ClientID=client_data['ClientID'])
        client_serializer=clientSerializer(client,data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        client=client.objects.get(ClientID=id)
        client.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)