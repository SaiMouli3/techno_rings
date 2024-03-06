from django.shortcuts import render, redirect
from .forms import EmployeeToolForm
from .models import Employee, Job


def create_employee_tool(request):
    if request.method == 'POST':
        form = EmployeeToolForm(request.POST)
        if form.is_valid():
            emp_ssn = form.cleaned_data['emp_ssn']
            emp_name = form.cleaned_data['emp_name']
            mobile = form.cleaned_data['mobile']
            address = form.cleaned_data['address']
            job_id = form.cleaned_data['job_id']
            job_name = form.cleaned_data['job_name']
            tool_code = form.cleaned_data['tool_code']
            tool_length = form.cleaned_data['tool_length']
            no_of_holes = form.cleaned_data['no_of_holes']

            employee = Employee.objects.create(
                emp_ssn=emp_ssn,
                emp_name=emp_name,
                mobile=mobile,
                address=address,
                emp_efficiency = 0
            )

            job = Job.objects.create(
                job_id = job_id,
                job_name = job_name,
                tool_code=tool_code,
                length=tool_length,
                no_of_holes=no_of_holes
            )

            return redirect('success_page')

    else:
        form = EmployeeToolForm()

    return render(request, 'webapp/pagel.html', {'form': form})



def success_page(request):
    return render(request, 'success_page.html')
