# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from person.models import Persondetails
from loan.models import Loandetails
from dateutil.relativedelta import relativedelta
from datetime import datetime
from .models import *


# Create your views here.
@api_view(['POST'])
def updateloandata(request):
    try:
        data = request.data
        Loandetails.objects.filter(id= data['loan']).update(loan_status='Approved')
        ln = Loandetails.objects.filter(id= data['loan'])
        ln_data = ln.values('repayment_amount','tenure','id')
        pn = Persondetails.objects.filter(id=data['person'])
        repayment_amount = ln_data[0]['repayment_amount']
        tenure = ln_data[0]['tenure']
        payable_amount = (repayment_amount/tenure)
        today = datetime.now().date()
        for i in range(1, tenure+1):
            lnobj = Loandata()
            lnobj.payable_amount = payable_amount
            lnobj.payable_date = today + relativedelta(months=i)
            print lnobj.payable_date
            lnobj.loan = ln[0]
            lnobj.person = pn[0]
            lnobj.payable_status = 'Pending'
            lnobj.save()

        return Response("Update Saved", status=status.HTTP_200_OK)
    except Exception as e:
        print e

        return Response(status=status.HTTP_401_UNAUTHORIZED)
