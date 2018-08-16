# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Loandetails
from bank.models import Bankdetails
from person.models import Persondetails


# Create your views here.
@api_view(['POST'])
def addloan(request):
    try:
        data = request.data
        data['person'] = Persondetails.objects.get(id=data['person'])
        data['bank'] = Bankdetails.objects.get(id=data['bank'])
        data['loan_amount'] = loan_amount = data['loan_amount']
        data['interest_rate'] = interest_rate = data['interest_rate']
        data['interest_amount'] = interest_amount = (loan_amount * interest_rate / 100) * data['tenure']
        data['repayment_amount'] = loan_amount + interest_amount
        data['loan_status'] = 'Pending'
        adobj = Loandetails(**data)

        adobj.save()

        return Response("Successfully saved", status=status.HTTP_200_OK)
    except Exception as e:
        print e

        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def getallloan(request):
    print "getting all data"
    data = Loandetails.objects.all().values()

    return Response(data)


@api_view(['POST'])
def getloan(request):
    try:
        loan_id = request.data['id']
        loan_obj = Loandetails.objects.filter(id=loan_id).values()
        output = "Record not found" if not loan_obj else loan_obj
        return Response(output, status=status.HTTP_200_OK)
    except Exception as e:
        print e

        return Response("Exception occurred",status=status.HTTP_401_UNAUTHORIZED)



@api_view(['DELETE'])
def deleteloan(request):
    id = request.data['id']
    print "id is", id
    d = Loandetails.objects.filter(id=id)
    d.delete()
    return Response("Deleted")


@api_view(['PUT'])
def updateloan(request):
    try:
        #balance = request.data['balance']
        id1 = request.data['id']
        tenure = request.data['tenure']
        Loandetails.objects.filter(id=id1).update(tenure=tenure)

        return Response("Successfully saved", status=status.HTTP_200_OK)
    except Exception as e:
        print e

        return Response("Update Failed", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def fetchloan(request):
    i_rate = request.data['interest_rate']
    d = Loandetails.objects.exclude(interest_rate=i_rate).values()
    return Response(d, status=status.HTTP_200_OK)

