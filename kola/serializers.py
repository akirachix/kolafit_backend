from rest_framework import serializers 
from .models import Customer
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