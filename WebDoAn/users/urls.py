from django.contrib import admin
from django.urls import path, include
from .views import (
                    register,
                    register_success)

urlpatterns = [
    path('register/', register, name='register'),
    
    #[test login] this path just for test login correctly 
    path('register-sucess/', register_success, name='register-success'),
]