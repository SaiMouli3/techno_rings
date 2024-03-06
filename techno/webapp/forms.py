from django import forms
from .models import Employee, Tool


class EmployeeForm(forms.Form):
    emp_ssn = forms.IntegerField()
    emp_name = forms.CharField(max_length=100)
    mobile = forms.CharField(max_length=10)
    address = forms.CharField(widget=forms.Textarea)


class JobForm(forms.Form):
    job_id = forms.IntegerField()
    job_name = forms.CharField(max_length=100)
    tool_code = forms.CharField(max_length=100)
    tool_length = forms.FloatField()
    no_of_holes = forms.IntegerField()


class MachineForm(forms.Form):
    machine_name = forms.CharField(max_length=100)
    job_name = forms.CharField(max_lenth=100)


