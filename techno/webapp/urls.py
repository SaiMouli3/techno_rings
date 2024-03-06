from django.urls import path
from .views import create_employee_tool, success_page

urlpatterns = [
    path('create/', create_employee_tool, name='create_employee_tool'),
    path('success/', success_page, name='success_page'),
]
