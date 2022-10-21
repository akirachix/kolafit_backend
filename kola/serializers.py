from rest_framework import serializers 
from .models import Customer
from django.contrib.auth.models import User
 
class CustomerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Customer
        fields = ("full_name", "gender", "email", 'password')


class CustomerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ( 'full_name', 'gender', 'email','password')
        extra_kwargs = {'password': {'write_only': True}}        
        
def create(self, validated_data):
        user = Customer.objects.create(validated_data['email'], validated_data['password'],)
        return user

# class CustomerLoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ("email", "password")        