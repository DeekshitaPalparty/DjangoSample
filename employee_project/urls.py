"""employee_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from employee_project.services.employee_service import *
from employee_project.services.login_service import *
from employee_project.services.file_services import *
from employee_project.services.customer_services import *

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('employee/',include('employee_register.urls')),
    path('employee/<int:id>/',EMPLOYEE_ADD,name='employee_post'),
    path('employee/list1/',EMPLOYEE_FETCH,name='employee_display'), # get and post req. for update operation
    path('employee/login/<int:id>/',EMPLOYEE_LOGIN_VALIDATE, name= 'login_validate'),
    path('auth/',obtain_auth_token),
    path('auth1/',EMPLOYEE_LOGIN_VALIDATE),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth1/reset/', Update_info,name ='reset password'),
    path('employee/datatransfer/',File_handler,name='file_upload'),
    path('employee/chunktransfer/',File_handler_chunks,name='file_upload'),
    path('customer/db/',Database_fetch,name='dbserver_details'),
    path('customer/add/',Customer_info,name ='add_customer')
]
