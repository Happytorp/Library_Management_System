from users_app import views
from django.urls import path

urlpatterns = [
    path('register', views.register, name ='register'),             #creating the urls patterns
    path('login', views.login, name ='login'),
    path('logout', views.logout, name ='logout'),
    
]