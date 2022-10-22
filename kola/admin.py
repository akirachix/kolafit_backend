from django.contrib import admin
from . import models

# Register your models here.
from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
 
    list_display = ("first_name" ,"last_name","gender", "email")

admin.site.register(Customer,CustomerAdmin)

