from rest_framework import serializers 
from .models import Customer, Bill, Identification, Loan
from django.contrib.auth.models import User
 
class CustomerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Customer
        fields = ("first_name","last_name","gender", "email", 'password')


class CustomerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name',"last_name", 'gender', 'email','password')
        extra_kwargs = {'password': {'write_only': True}}        
        
def create(self, validated_data):
        user = User.objects.create(validated_data['first_name'],validated_data['last_name'],validated_data['email'], validated_data['password'])
        return user

class CustomerLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("email", "password")   

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ("customer", "rent_amount", "bills", "electricity_picture", "water_picture", "bills_amount")  


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ("customer","amount")                    

class IdentificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identification
        fields =  ("customer" , "id_number", "id_picture")

       