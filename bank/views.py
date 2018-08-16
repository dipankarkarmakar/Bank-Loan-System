from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Bankdetails

# Create your views here.
@api_view(['POST'])
def addbank(request):
    try:
        adobj=Bankdetails(**request.data)
        adobj.save()

        return Response("Successfully saved", status=status.HTTP_200_OK)
    except Exception as e:
        print e

        return Response(status=status.HTTP_401_UNAUTHORIZED)
#
# def persons():
#     return Response(status=200)


@api_view(['GET'])
def getallbank(request):

     print "getting all data"
     data = Bankdetails.objects.all().values()

     return Response(data)



@api_view(['POST'])
def getbank(request):
    try:
        bank_id = request.data['id']
        bank_obj = Bankdetails.objects.filter(id=bank_id).values()
        output = "Record not found" if not bank_obj else bank_obj
        return Response(output, status=status.HTTP_200_OK)
    except Exception as e:
        print e

        return Response("Exception occurred",status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT'])
def updatebank(request):
    try:
        mobile_number = request.data['mobile_number']
        id = request.data['id']
        Bankdetails.objects.filter(id=id).update(mobile_number=mobile_number)

        return Response("Successfully saved", status=status.HTTP_200_OK)
    except Exception as e:
        print e

        return Response("Update Failed", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['DELETE'])
def delbank(request):
    id = request.data['id']
    print "id is", id
    d = Bankdetails.objects.filter(id=id)
    d.delete()
    return Response("Deleted")





