# from .views import CustomerLoginView
from knox import views as knox_views
from django.urls import path, include
from . import views



urlpatterns = [
    # path("request_loan/", views.Loan_Eligibility.as_view(), name="loan_eligibility"),
    
    
]



