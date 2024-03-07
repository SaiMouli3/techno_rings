from django.urls import path
from .views import employee_create_view, tool_create_view,success_page, job_create_view

urlpatterns = [
    path('employee_create/', employee_create_view, name='employee_create_view'),
    path('tool_create/', tool_create_view, name='tool_create_view'),
    path('job_create/', job_create_view, name='job_create_view'),
    path('success_page/', success_page, name='success_page'),
]
