from django.urls import path
from . import views

url_patterns = [
    path('login/', views.user_login, name='login'),

]