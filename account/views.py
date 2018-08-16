# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Accountdetails
from bank.models import Bankdetails
from person.models import Persondetails

from django.shortcuts import render

# Create your views here.
@api_view(['POST'])
def addaccount(request):
    try:
        request.data['person'] = Persondetails.objects.get(id=request.data['person'])
        request.data['bank'] = Bankdetails.objects.get(id=request.data['bank'])
        adobj=Accountdetails(**request.data)

        adobj.save()

        return Response("Successfully saved", status=status.HTTP_200_OK)
    except Exception as e:
        print e

        return Response(status=status.HTTP_401_UNAUTHORIZED)



@api_view(['GET'])
def getallaccount(request):

     print "getting all data"
     data = Accountdetails.objects.all().values()

     return Response(data)


@api_view(['POST'])
def getaccount(request):
    try:
        get_id = request.data['id']
        get_obj = Accountdetails.objects.filter(id=get_id).values('balance')
        output = "Record not found" if not get_obj else get_obj
        return Response(output, status=status.HTTP_200_OK)
    except Exception as e:
        print e

        return Response("Exception occurred",status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT'])
def updateaccount(request):
    try:
        balance = request.data['balance']
        id = request.data['id']
        Accountdetails.objects.filter(id=id).update(balance=balance)

        return Response("Successfully saved", status=status.HTTP_200_OK)
    except Exception as e:
        print e

        return Response("Update Failed", status=status.HTTP_401_UNAUTHORIZED)



@api_view(['DELETE'])
def delaccount(request):
    id = request.data['id']
    print "id is", id
    d = Accountdetails.objects.filter(id=id)
    d.delete()
    return Response("Deleted")


# @api_view(['GET'])
# def nameaccount(request):

#     d = accountdetails.objects.filter().values('person')
#     return Response(d)
'''this will give me id of the persons who have bank a/c in dictionary format'''

@api_view(['GET'])
def nameaccount(request):

    d = Accountdetails.objects.filter().values_list('person',flat=True)
#'''this will give me id of the persons who have bank a/c in list format'''
    p=Persondetails.objects.filter(id__in=d).values('name')
#'''this will give me name of the persons who have bank a/c in list format'''

    return Response(p)


@api_view(['GET'])
def fetchaccount(request):
    # d = accountdetails.objects.filter().values_list('person', flat=True)
    # p = persondetails.objects.exclude(id__in=d).values('name')
    names = Accountdetails.objects.filter().values_list('person__name', flat=True)
    return Response(names)
