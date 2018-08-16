from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Persondetails
# Create your views here.


@api_view(['POST'])
def addperson(request):
    try:
        print "request.data: ", request.data
        addob=Persondetails(**request.data)
        addob.save()

        return Response("Successfully saved", status=status.HTTP_200_OK)
    except Exception as e:
        print e

        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def getallperson(request):

     print "getting all data"
     data = Persondetails.objects.all().values()

     return Response(data)


@api_view(['POST'])
def getperson(request):
    try:
        person_id = request.data['id']
        person_obj = Persondetails.objects.filter(id=person_id).values()
        output = "Record not found" if not person_obj else person_obj
        return Response(output, status=status.HTTP_200_OK)
    except Exception as e:
        print e

        return Response("Exception occurred",status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT'])
def updateperson(request):
    try:
        mobile_number = request.data['mobile_number']
        id = request.data['id']
        Persondetails.object.filter(id=id).update(mobile_number=mobile_number)

        return Response("Successfully saved", status=status.HTTP_200_OK)
    except Exception as e:
        print e

        return Response("Update Failed", status=status.HTTP_401_UNAUTHORIZED)



@api_view(['DELETE'])
def delperson(request):
    id = request.data['id']
    print "id is", id
    d = Persondetails.objects.filter(id=id)
    d.delete()
    return Response("Deleted")
