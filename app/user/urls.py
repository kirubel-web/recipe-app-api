"""
URL mappings for the user API
"""
from django.urls import path
from user import views


aspp_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
]
