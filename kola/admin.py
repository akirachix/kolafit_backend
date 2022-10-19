from django.contrib import admin

# Register your models here.
from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
 
    list_display = ("full_name", "gender", "email")

admin.site.register(Customer,CustomerAdmin)