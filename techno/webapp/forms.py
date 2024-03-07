from django import forms
from .models import Employee, Tool


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_ssn', 'emp_name', 'mobile', 'address']


class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['tool_code', 'tool_name', 'max_length', 'cost', 'length_cut', 'no_of_brk_points']
