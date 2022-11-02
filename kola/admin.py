from django.contrib import admin
from . import models

# Register your models here.
from .models import Customer, Detail,Identification
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name" ,"last_name","gender", "email", "password")
admin.site.register(Customer,CustomerAdmin)


class DetailAdmin(admin.ModelAdmin):
    list_display = ("customer", "rent_amount", "rent_receipts", "electricity_receipts", "water_receipts", "loan_amount")
admin.site.register(Detail , DetailAdmin)    


class IdentificationAdmin(admin.ModelAdmin):
    list_display = ("customer" ,"location", "id_number" , "id_picture")
admin.site.register(Identification,IdentificationAdmin)


