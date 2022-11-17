from django.contrib import admin
from . import models

# Register your models here.
from .models import Customer, Detail,Identification
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name" ,"last_name","gender", "email", "password", "confirm_password")
admin.site.register(Customer,CustomerAdmin)


class DetailAdmin(admin.ModelAdmin):
    list_display = ("customer", "rent_amount", "electricity_bill", "water_bill", "loan_amount")
admin.site.register(Detail , DetailAdmin)    


class IdentificationAdmin(admin.ModelAdmin):
    list_display = ("customer" ,"location", "id_number", "id_picture")
admin.site.register(Identification,IdentificationAdmin)


