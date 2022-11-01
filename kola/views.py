from dataclasses import dataclass
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets 
from .serializers import CustomerSerializer, CustomerRegisterSerializer,CustomerLoginSerializer, DetailSerializer, IdentificationSerializer
from .models import Customer,Detail, Identification
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import generics, permissions
from django.contrib.auth import login,authenticate
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import status

from kola import serializers

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

     
class DetailView(viewsets.ModelViewSet):
    queryset = Detail.objects.all() 
    serializer_class =   DetailSerializer   


class IdentificationView(viewsets.ModelViewSet):
    queryset=Identification.objects.all()
    serializer_class = IdentificationSerializer
    def customer_identification(request):
        if request.method == "POST":
            serializer = IdentificationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201) 


           
            

