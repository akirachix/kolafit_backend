from dataclasses import dataclass
from rest_framework import views
import json
from telnetlib import LOGOUT
from xml.dom import ValidationErr
from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets 
from .serializers import CustomerSerializer, CustomerRegisterSerializer,CustomerLoginSerializer, DetailSerializer, IdentificationSerializer
from .models import Customer,Detail, Identification
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import generics, permissions
from django.contrib.auth import login,authenticate
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from kola import serializers
from rest_framework.decorators import api_view, permission_classes
# from django.core.exceptions import ValidationError
# from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.hashers import check_password
from django.db import IntegrityError

class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    
    def register_customer(request):
        if request.method == "POST":
            serializer = CustomerRegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)   


class CustomerLoginView(viewsets.ModelViewSet):
    serializer_class = CustomerLoginSerializer
    queryset = Customer.objects.all()

   



# @api_view(["GET"])
# # @permission_classes([IsAuthenticated])
# def User_logout(request):

#     request.user.auth_token.delete()

#     LOGOUT(request)

#     return Response('User Logged out successfully')            

     
class DetailView(viewsets.ModelViewSet):
    queryset = Detail.objects.all() 
    serializer_class =   DetailSerializer  
    parser_classes = (MultiPartParser, FormParser) 
    def customer_detail(request):
        if request.method == "POST":
            serializer = DetailSerializer(data=request.data)
            if serializer.is_valid():
                Detail.objects.create(
                rent_amount=request.POST.get('rent_amount'),
                rent_receipts=request.POST.get('media/rent_receipts/'),
                electricity_receipts=request.POST.get('media/electricity_receipts/'),
                water_receipts=request.POST.get('media/water_receipts/'),
                loan_amount=request.POST.get('loan_amount'),
                )
                serializer.save()
                return Response(serializer.data, status=201)   



class IdentificationView(viewsets.ModelViewSet):
    queryset=Identification.objects.all()
    serializer_class = IdentificationSerializer
    parser_classes = (MultiPartParser, FormParser)
    
    def customer_identification(request):
        if request.method == "POST":
            serializer = IdentificationSerializer(data=request.data)
            if serializer.is_valid():
                Identification.objects.create(
                location=request.POST.get('location'),
                id_number=request.POST.get('id_number'),
                id_picture=request.POST.get('id_picture'),
                )
                serializer.save()
                return Response(serializer.data, status=201) 

class Loan_Eligibility(views.APIView):
    def post(self, request, format=None):       
       income = round(float(request.data["income"]))
       rent_receipts = request.data["rent_receipts"]
       electricity_receipts= request.data["electricity_receipts"]
       water_receipts = request.data["water_receipts"]
       fixed_obligations = rent_receipts + electricity_receipts + water_receipts
       loan_amount = round(float(request.data["loan_amount"]))
       disposable_income_for_loan = income - fixed_obligations

       probability = (disposable_income_for_loan / income) * 100
       print(probability)
       if probability > 50 and loan_amount <= disposable_income_for_loan:
        return Response (f"Congratulations {Customer}, you are eligible for ksh {loan_amount}.")
       else:
        return Response (f"We are sorry {Customer}, you are not eligible for ksh {loan_amount}, please try applying for a lower amount.")


       try:
           customer = Customer.objects.get("customer")
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.buy_airtime(amount)
       return Response(message, status=status)     




           
            

