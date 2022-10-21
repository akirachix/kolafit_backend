from rest_framework import serializers 
from .models import Customer
 
class CustomerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Customer
        fields = ("full_name", "gender", "email", 'password')

# class CustomerLoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ("email", "password")