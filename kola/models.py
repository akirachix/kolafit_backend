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
    
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

# lets us explicitly set upload path and filename
def upload_to(filename):
    return 'images/'.format(filename=filename)

class Identification(models.Model):
    customer=models.ForeignKey(on_delete=models.CASCADE,to=Customer) 
    location=models.CharField(max_length=50, null=True)  
    id_number=models.IntegerField(unique=True)  
    id_picture=models.ImageField(upload_to=upload_to("id_pics"), blank=True, null=True) 
      
class Detail(models.Model):
    customer = models.ForeignKey(on_delete=models.CASCADE,to=Customer)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    rent_receipts= models.ImageField(upload_to=upload_to("rent_receipts"), blank=True, null=True)
    electricity_receipts=models.ImageField(upload_to=upload_to("electricity_receipts"),blank=True, null=True) 
    water_receipts=models.ImageField(upload_to=upload_to("water_receipts"), blank=True, null=True) 
    loan_amount=models.DecimalField(max_digits=10, decimal_places=2)
   

