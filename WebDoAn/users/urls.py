from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    
    #[test login] this path just for test login correctly 
    path('', home, name='home'),
    path('profile/<int:id>/', ProfileDetailView.as_view(), name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]