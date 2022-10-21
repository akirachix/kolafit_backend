from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
from rest_framework import viewsets 
from .serializers import CustomerSerializer 
from .models import Customer 
# import json

class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

# class CustomerLoginView(viewsets.ModelViewSet):
#     serializer_class = CustomerLoginSerializer
#     queryset = Customer.objects.all()

# @csrf_exempt
# def signUp(request):
#     if request.method == "POST":
#         customer_data = json.parse(request)
#         customer_seralizer = CustomerSerializer(data=customer_data)
#         if customer_seralizer.is_valid():
#             customer_seralizer.save()
#             return JsonResponse("Added customer")
#         return JsonResponse("Failed to add customer")        