import json
# from telnetlib import LOGOUT
from xml.dom import ValidationErr
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
# from django.core.exceptions import ValidationError
# from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.hashers import check_password
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions, status, views, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.parsers import FormParser, MultiPartParser,JSONParser,FileUploadParser
from rest_framework.permissions import AllowAny
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,
                                   HTTP_404_NOT_FOUND)
from rest_framework.views import APIView
# from rest_framework.decorators import action
from kola import serializers
from rest_framework import viewsets

from .models import Customer, Detail, Identification
from .serializers import (CustomerLoginSerializer, CustomerRegisterSerializer,
                           DetailSerializer,
                          IdentificationSerializer)


class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerRegisterSerializer
    queryset = Customer.objects.all()
    
    def create(self,request):
        serializer = CustomerRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)     
               

class CustomerLoginView(viewsets.ModelViewSet):
    serializer_class = CustomerLoginSerializer
    queryset = Customer.objects.all()
    
    def login(request):
        serializer = CustomerLoginSerializer(data=validated_data)
        if serializer.is_valid():
            serializer.save()
        validated_data= serializer.validated_data
        email = validated_data.get("email")
        password = validated_data.get("password")
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key},
            status=HTTP_200_OK)             
           

class IdentificationView(viewsets.ModelViewSet):
    queryset=Identification.objects.all()
    serializer_class = IdentificationSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)


    def create(self, request, format=None):
        data = request.data
        if isinstance(data, list):  # <- is the main logic
            serializer = IdentificationSerializer(data=request.data, many=True)
        else:
            serializer = IdentificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    



class DetailView(viewsets.ModelViewSet):
    queryset = Detail.objects.all() 
    serializer_class =   DetailSerializer  
    parser_classes = (MultiPartParser, FormParser, JSONParser, FileUploadParser) 
    def create(self, request):
            serializer = DetailSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            validated_data= serializer.validated_data
            income = validated_data.get("income")
            rent_amount = validated_data.get("rent_amount")
            electricity_bill= validated_data.get("electricity_bill")
            water_bill = validated_data.get("water_bill")

            fixed_obligations = rent_amount + electricity_bill + water_bill
            loan_amount =validated_data.get("loan_amount")
            disposable_income_for_loan = income - fixed_obligations

            probability = (disposable_income_for_loan / income) * 100
            customer = validated_data.get("customer")
            if probability > 50 and loan_amount <= disposable_income_for_loan:
                return Response (f"Congratulations {customer.first_name}, you are eligible for Ksh {loan_amount}.")
            return Response (f"We are sorry {customer.first_name}, you are not eligible for Ksh {loan_amount}, you can apply for Ksh {disposable_income_for_loan}.")  

 
        
   




           
            

