from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
 
from .serializers import CustomerSerializer
 
from .models import Customer
 
class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()