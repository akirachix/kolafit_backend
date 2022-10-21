from django.db import models

# Create your models here.
class Customer(models.Model):
    full_name=models.CharField(max_length=50,null=True)
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    )
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)
    email = models.EmailField(null = True)
    password=models.CharField(max_length = 15,null=True)

    def __str__(self):
         return self.full_name

