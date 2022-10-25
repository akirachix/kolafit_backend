from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets 
from .serializers import CustomerSerializer, CustomerRegisterSerializer,CustomerLoginSerializer, BillSerializer
from .models import Customer, Bill
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

class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class CustomerLoginView(viewsets.ModelViewSet):
    serializer_class = CustomerLoginSerializer
    queryset = Customer.objects.all()

@csrf_exempt
def signUpApi(request,id=0):
    if request.method=='GET':
        customers = Customer.objects.all()
        customer_serializer = CustomerSerializer(customers,many=True)
        return JsonResponse(customer_serializer.data,safe=False)

    elif request.method=='POST':
        customer_data = JSONParser().parse(request)
        breakpoint()
        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method=='PUT':
        customer_data=JSONParser().parse(request)
        customer = Customer.objects.get(first_name = customer_data.first_name)
        customer_serializer=CustomerSerializer(customer,data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)
    
    elif request.method=='DELETE':
        customer=Customer.objects.get(first_name = customer.first_name)
        customer.delete()
        return JsonResponse("Deleted successfully",safe=False)


# class CustomerRegisterAPI(generics.GenericAPIView):
#     serializer_class = CustomerRegisterSerializer
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         customer = serializer.save()
#         User.objects.create_user(first_name=customer.first_name , password=customer.password)
#         return Response({
#         "customer": CustomerSerializer(customer, context=self.get_serializer_context()).data,
#         })

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = CustomerRegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer = serializer.save()
        User.objects.create_user(email=customer.email , password=customer.password)
        return Response({
        "customer": CustomerSerializer(customer, context=self.get_serializer_context()).data,
        })
# class LoginAPI(ObtainAuthToken):
#     permission_classes = (permissions.AllowAny)
#     def post(self, request, format=None):
#         email=request.data['email']
        # password=request.data['password']
        # user=authenticate(request,email=email, password=password)
        # print(user)
        # token=Token.objects.create(user=user)
        # return Response({
        #     'body': 'login successful',
        #     "token": token.key
        # ertyujkil;''
#         })
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        username=request.data['email']
        password=request.data['password']
        user=authenticate(request,email=username, password=password)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user=user)
        return user(LoginAPI, self).post(request, format=None)

class BillView(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer        