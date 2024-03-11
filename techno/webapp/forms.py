from django import forms
from .models import Employee, Tool, Job, Machine


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_ssn', 'emp_name', 'mobile', 'address']


class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['tool_code', 'tool_name', 'max_length', 'cost', 'length_cut']


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['job_id', 'job_name','tools']

    tools = forms.ModelMultipleChoiceField(
        queryset=Tool.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['machine_id', 'machine_name', 'jobs', 'tool_name']

    jobs = forms.ModelMultipleChoiceField(
        queryset=Job.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
