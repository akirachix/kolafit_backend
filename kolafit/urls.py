"""kolafit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from kola import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'signup',views.CustomerView, 'signup')
# router.register(r'login',views.CustomerLoginView, 'login')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]

 


#  from django.urls import path
# from . import views
# from knox import views as knox_views


# urlpatterns = [
#     path('teachers/',views.teacherApi, name='teachers' ),
#     path('login/', views.LoginAPI.as_view(), name='login'),
#     path('registerteacher/', views.TeacherRegisterAPI.as_view(), name='registerTeacher'),
#     path('students',views.studentApi,name='students'),
#     path('register/',views.RegisterAPI.as_view(), name='register'),
#     # path('Quicklab/logout/', knox_views.LogoutView.as_view(), name='logout'),
#     # path('Quicklab/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
# ]
 
