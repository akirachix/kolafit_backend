import json
from dataclasses import dataclass
# from telnetlib import LOGOUT
from xml.dom import ValidationErr

from django.contrib.auth import authenticate, login
# from django.core.exceptions import ValidationError
# from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.hashers import check_password
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
# from django.http import HttpResponse, JsonResponse
from rest_framework import generics, permissions, status, views, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,
                                   HTTP_404_NOT_FOUND)
from rest_framework.views import APIView

from kola import serializers

from .models import Customer, Detail, Identification
from .serializers import (CustomerLoginSerializer, CustomerRegisterSerializer,
                          CustomerSerializer, DetailSerializer,
                          IdentificationSerializer)



class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    
    def register_customer(request):
        if request.method == "POST":
            serializer = CustomerRegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)  


# @csrf_exempt
# @api_view(["POST"])
# # @permission_classes((AllowAny,))
# def login(request):
#     serializer_class = CustomerLoginSerializer
#     email = request.data.get("email")
#     password = request.data.get("password")
#     if email is None or password is None:
#         return Response({'error': 'Please provide both username and password'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = authenticate(email=email, password=password)
#     if not user:
#         return Response({'error': 'Invalid Credentials'},
#                         status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key},
#                     status=HTTP_200_OK)                 

class CustomerLoginView(viewsets.ModelViewSet):
    serializer_class = CustomerLoginSerializer
    queryset = Customer.objects.all()
    
    def login(request):
        if request.method == "POST":
            username = request.data.get("email")
            password = request.data.get("password")
            if username and password:
                queryset = queryset.filter(username=username)
                if queryset.exists():
                    user = authenticate(username=username, password=password)
                    token, _ = Token.objects.get_or_create(user=user)
                    return Response({'token': token.key},
                    status=HTTP_200_OK)             

     
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
                # rent_receipts=request.POST.get('media/rent_receipts/'),
                electricity_bill=request.POST.get('elecricity_bill'),
                water_bill=request.POST.get('water_bill'),
                loan_amount=request.POST.get('loan_amount'),
                )
                serializer.save()
                return Response(serializer.data, status=201)  

    def loan_eligibility(self, request, format=None):
        income = (request.data["income"])
        rent_amount = request.data["rent_amount"]
        electricity_bill= request.data["electricity_bill"]
        water_bill = request.data["water_bill"]
        fixed_obligations = rent_amount + electricity_bill + water_bill
        loan_amount =(request.data["loan_amount"])
        disposable_income_for_loan = income - fixed_obligations

        probability = (disposable_income_for_loan / income) * 100
        print(probability)
        if probability > 50 and loan_amount <= disposable_income_for_loan:
            return Response (f"Congratulations {Customer}, you are eligible for ksh {loan_amount}.")
        else:
            return Response (f"We are sorry {Customer}, you are not eligible for ksh {loan_amount}, please try applying for a lower amount.")             



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

# class Loan_Eligibility(views.APIView):
#     def post(self, request, format=None):       
#        income = round(float(request.data["income"]))
#        rent_receipts = request.data["rent_receipts"]
#        electricity_receipts= request.data["electricity_receipts"]
#        water_receipts = request.data["water_receipts"]
#        fixed_obligations = rent_receipts + electricity_receipts + water_receipts
#        loan_amount = round(float(request.data["loan_amount"]))
#        disposable_income_for_loan = income - fixed_obligations

#        probability = (disposable_income_for_loan / income) * 100
#        print(probability)
#        if probability > 50 and loan_amount <= disposable_income_for_loan:
#         return Response (f"Congratulations {Customer}, you are eligible for ksh {loan_amount}.")
#        else:
#         return Response (f"We are sorry {Customer}, you are not eligible for ksh {loan_amount}, please try applying for a lower amount.")

        
   




           
            

