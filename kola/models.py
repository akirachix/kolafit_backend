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
    email = models.EmailField(null = True)
    password=models.CharField(max_length = 15,null=True)
    
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Identification(models.Model):
    customer=models.ForeignKey(on_delete=models.CASCADE,to=Customer) 
    id_number=models.IntegerField(unique=True)  
    id_picture=models.ImageField(default='default.jpg', upload_to='id_pics') 


class Bill(models.Model):
    customer = models.ForeignKey(on_delete=models.CASCADE,to=Customer)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    BILLS_CHOICES=(
        ('E','Electricity'),
        ('W','Water'),
    )
    bills = models.CharField(max_length=30,choices=BILLS_CHOICES,null=True)
    electricity_picture=models.ImageField(default='default.jpg', upload_to='electricity_pics') 
    water_picture=models.ImageField(default='default.jpg', upload_to='water_pics') 
   
    bills_amount=models.DecimalField(max_digits=10, decimal_places=2)

    
class Loan(models.Model):
    customer = models.ForeignKey(on_delete=models.CASCADE,to=Customer)
    amount=models.DecimalField(max_digits=10,decimal_places=2)    

