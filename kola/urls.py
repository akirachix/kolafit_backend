from .views import CustomerLoginView
from knox import views as knox_views
from django.urls import path

urlpatterns = [
    # path('api/register/', RegisterAPI.as_view()),
    # path('login/',CustomerLoginView.as_view()),
    # path('api/logout/', knox_views.LogoutView.as_view()),
    # path('api/logoutall/', knox_views.LogoutAllView.as_view()),
    # # path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),

]

