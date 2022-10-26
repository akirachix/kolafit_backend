from django.contrib import admin
from . import models

# Register your models here.
from .models import Customer, Bill,Identification,Loan
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name" ,"last_name","gender", "email")
admin.site.register(Customer,CustomerAdmin)


class BillAdmin(admin.ModelAdmin):
    list_display = ("customer", "rent_amount", "bills", "electricity_picture", "water_picture", "bills_amount")
admin.site.register(Bill , BillAdmin)    


class IdentificationAdmin(admin.ModelAdmin):
    list_display = ("customer" , "id_number" , "id_picture")
admin.site.register(Identification,IdentificationAdmin)


class LoanAdmin(admin.ModelAdmin):
    list_display = ("customer","amount")
admin.site.register(Loan , LoanAdmin)    

