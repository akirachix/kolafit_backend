
from rest_framework import serializers 
from .models import Customer, Detail, Identification
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name","last_name","gender", "email","password")


class CustomerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name',"last_name", "gender", "email","password", "confirm_password")
        extra_kwargs = {"password": {"write_only": True}}
    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
            {"password": "Password fields didn't match."})
        return attrs        
        
    def create(self, validated_data):
        customer = Customer.objects.create(validated_data["first_name"],
        validated_data["last_name"],
        validated_data["email"])
        customer.set_password(validated_data['password'])
        customer.save()
        return customer


class CustomerLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("email", "password") 
    def get(self, request, format=None):
        username=request.data['email']
        password=request.data['password']
        queryset = Customer.objects.all()
        if username and password:
            queryset = queryset.filter(username=username)
            if queryset.exists():
                user = Customer.objects.get(username=username)
                if user.check_password(password):
                    return Response(CustomerSerializer(queryset, many=True).data, status=status.HTTP_200_OK)


class DetailSerializer(serializers.ModelSerializer):
    rent_receipts = serializers.ImageField(required=False)
    electricity_receipts = serializers.ImageField(required=False)
    water_receipts = serializers.ImageField(required=False)
    class Meta:
        model = Detail
        fields = ("customer","rent_amount", "rent_receipts", "electricity_receipts", "water_receipts", "loan_amount")  
        # extra_kwargs = {"password": {"write_only": True}}
              
       
                   

class IdentificationSerializer(serializers.ModelSerializer):
    id_picture = serializers.ImageField(required=False)
    class Meta:
        model = Identification
        fields =  ("customer","location","id_number", "id_picture")
    


       