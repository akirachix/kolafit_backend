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


    # def post(self, request, format=None):
    #     serializer = AuthTokenSerializer(data=request.data)
    #     username=request.data['email']
    #     password=request.data['password']
    #     user=authenticate(request,username=username, password=password)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.validated_data['user']
    #     login(request, user=user)
    #     return user(CustomerLoginView, self).post(request, format=None)


# class LoginAPI(KnoxLoginView):
#     permission_      classes = (permissions.AllowAny,)

    # def post(self, request, format=None):
    #     serializer = AuthTokenSerializer(data=request.data)
    #     username=request.data['email']
    #     password=request.data['password']
    #     user=authenticate(request,username=username, password=password)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.validated_data['user']
    #     login(request, user=user)
    #     return user(LoginAPI, self).post(request, format=None)


     
class DetailView(viewsets.ModelViewSet):
    queryset = Detail.objects.all() 
    serializer_class =   DetailSerializer   

class IdentificationAPI(generics.GenericAPIView):
    serializer_class = IdentificationSerializer
    def post(self,request,*args ,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        identification = serializer.save()
        User.objects.create_user(id_number=identification.id_number, location=identification.location, id_picture=identification.id_picture)
        return Response({
        "identification": IdentificationSerializer(identification, context=self.get_serializer_context()).data,
        })   


class IdentificationView(viewsets.ModelViewSet):
    queryset=Identification.objects.all()
    serializer_class = IdentificationSerializer