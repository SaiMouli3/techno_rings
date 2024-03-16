from django.urls import path
from .views import employee_create_view, tool_create_view, success_page, job_create_view, employee_delete_view, \
    tool_delete_view, job_delete_view, employee_update_view, tool_update_view, job_update_view, create_machine, \
    get_csrf_token, EmployeeCreateView, performs_data, JobsList, BreakdownList, update_employee
from .views1 import get_tool_names
from .views import EmployeeList
urlpatterns = [
    path('employee_create/', employee_create_view, name='employee_create_view'),
    path('tool_create/', tool_create_view, name='tool_create_view'),
    path('job_create/', job_create_view, name='job_create_view'),
    path('success_page/', success_page, name='success_page'),
    path('create_machine/', create_machine, name='create_machine'),
    path('get_tool_names/', get_tool_names, name='get_tool_names'),

    path('api/employees/', EmployeeList.as_view(), name='employee-list'),
    path('api/employees/create/',EmployeeCreateView.as_view(), name='employee-list-create'),
    path('api/jobs',JobsList.as_view(),name='job-list'),
    path('api/csrf-token/', get_csrf_token, name='get_csrf_token'),
    path('api/performs/', performs_data, name='performs_data'),
    path('api/breakdown',BreakdownList.as_view(),name='breakdown-data'),
    path('api/employees/<str:ssn>/', update_employee),

    path('employee/<int:emp_ssn>/delete/', employee_delete_view, name='employee_delete_view'),
    path('tool/<str:tool_code>/delete/', tool_delete_view, name='tool_delete_view'),
    path('job/<int:job_id>/delete/', job_delete_view, name='job_delete_view'),

    path('employee/<int:emp_ssn>/update/', employee_update_view, name='employee_update_view'),
    path('tool/<str:tool_code>/update/', tool_update_view, name='tool_update_view'),
    path('job/<int:job_id>/update/', job_update_view, name='job_update_view'),
]
