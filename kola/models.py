from enum import unique

from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=16,null=True)
    last_name=models.CharField(max_length=16, null=True)
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    )
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES,null=True)
    email = models.EmailField(unique= True,null = True)
    password=models.CharField(max_length = 15,null=True)
    confirm_password=models.CharField(max_length = 15,null=True)
    USERNAME_FIELD = ['email']
    REQUIRED_FIELDS = ['email', 'password']
    def __str__(self): 
        return '{} {}'.format(self.first_name, self.last_name)


class Identification(models.Model):
    customer=models.ForeignKey(on_delete=models.CASCADE,to=Customer) 
    location=models.CharField(max_length=50, null=True)  
    id_number=models.IntegerField(unique=True)  
    
      
class Detail(models.Model):
    customer = models.ForeignKey(on_delete=models.CASCADE,to=Customer)
    income=models.DecimalField(max_digits=10, decimal_places=2,null=True)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    electricity_bill=models.DecimalField(max_digits=10, decimal_places=2, null=True) 
    water_bill=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    loan_amount=models.DecimalField(max_digits=10, decimal_places=2, null=True)



   

