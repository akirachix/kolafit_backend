
from urllib import request

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator

from .models import Customer, Detail, Identification


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
        user = Customer.objects.create(validated_data["first_name"],
        validated_data["last_name"],
        validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return user


class CustomerLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("email", "password")
                    


class DetailSerializer(serializers.ModelSerializer):
    # rent_receipts = serializers.ImageField(required=False)
    # electricity_receipts = serializers.ImageField(required=False)
    # water_receipts = serializers.ImageField(required=False)
    class Meta:
        model = Detail
        fields = ("customer","rent_amount","electricity_bill", "water_bill", "loan_amount")  
        
              
       
                   

class IdentificationSerializer(serializers.ModelSerializer):
    # id_picture = serializers.ImageField(required=False)
    class Meta:
        model = Identification
        fields =  ("customer","location","id_number")
    


       