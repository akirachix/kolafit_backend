
from urllib import request

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator

from .models import Customer, Detail, Identification



class CustomerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name","last_name", "gender", "email","password", "confirm_password")
        extra_kwargs = {"password": {"write_only": True}}
        
    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
            {"password": "Password fields didn't match."})
        return attrs        


class CustomerLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("email", "password")
                    


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = '__all__' 
        
              
       
                   

class IdentificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identification
        fields =  '__all__'
    


       