from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm, ToolForm, JobForm, MachineForm
from .models import Employee, Tool, Job, Machine
from rest_framework import generics
from .serializers import EmployeeSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from django.middleware.csrf import get_token



def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCreateView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        serializer = EmployeeSerializer(data=data)

        if serializer.is_valid():
            new_employee = serializer.save()
            return JsonResponse({
                'emp_ssn': new_employee.emp_ssn,
                'emp_name': new_employee.emp_name,
                'address': new_employee.address,
                'mobile': new_employee.mobile,
                'emp_efficiency': new_employee.emp_efficiency,
            })
        else:
            return JsonResponse({'error': 'Invalid form data'}, status=400)


class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


def employee_create_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/webapp/success_page/')
    else:
        form = EmployeeForm()

    return render(request, 'webapp/employee_form.html', {'form': form})


def tool_create_view(request):
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/webapp/success_page/')
    else:
        form = ToolForm()

    return render(request, 'webapp/tool_form.html', {'form': form})


def job_create_view(request):
    if request.method == 'POST':
        job_id = request.POST.get('job_id')
        job_name = request.POST.get('job_name')

        selected_tools = request.POST.getlist('tools')
        for tool_code in selected_tools:
            length_field = f'length_{tool_code}'
            holes_field = f'no_of_holes_{tool_code}'
            length = request.POST.get(length_field)
            no_of_holes = request.POST.get(holes_field)

            tool = get_object_or_404(Tool, tool_code=tool_code)

            # Create the Job instance with the Tool reference and save it
            job = Job.objects.create(job_id=job_id, job_name=job_name, length=length, no_of_holes=no_of_holes, tool_code=tool)
            job.save()

        return redirect('success_page')  # Replace 'success_page' with the actual URL or view name
    else:
        # Retrieve tools for displaying in the form
        tools = Tool.objects.all()

    return render(request, 'webapp/job_form.html', {'tools': tools})


def create_machine(request):
    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():
            machine = form.save(commit=False)
            machine.save()
            form.save_m2m()  # Save the many-to-many relationships

            return redirect('success_page')  # Replace 'success_page' with the actual URL or view name
    else:
        form = MachineForm()

    jobs = Job.objects.all()

    return render(request, 'webapp/machine_form.html', {'form': form, 'jobs': jobs})


def employee_delete_view(request, emp_ssn):
    employee = get_object_or_404(Employee, emp_ssn=emp_ssn)

    if request.method == 'POST':
        employee.delete()
        return redirect('/webapp/success_page/')

    return render(request, 'webapp/employee_delete.html', {'employee': employee})


def tool_delete_view(request, tool_code):
    tool = get_object_or_404(Tool, tool_code=tool_code)

    if request.method == 'POST':
        tool.delete()
        return redirect('/webapp/success_page/')

    return render(request, 'webapp/tool_delete.html', {'tool': tool})


def job_delete_view(request, job_id):
    job = get_object_or_404(Job, job_id=job_id)

    if request.method == 'POST':
        job.delete()
        return redirect('/webapp/success_page/')

    return render(request, 'webapp/job_delete.html', {'job': job})


def employee_update_view(request, emp_ssn):
    employee = get_object_or_404(Employee, emp_ssn=emp_ssn)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/webapp/success_page/')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'webapp/employee_update.html', {'form': form})


def tool_update_view(request, tool_code):
    tool = get_object_or_404(Tool, tool_code=tool_code)

    if request.method == 'POST':
        form = ToolForm(request.POST, instance=tool)
        if form.is_valid():
            form.save()
            return redirect('/webapp/success_page/')
    else:
        form = ToolForm(instance=tool)

    return render(request, 'webapp/tool_update.html', {'form': form})


def job_update_view(request, job_id):
    job = get_object_or_404(Job, job_id=job_id)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('/webapp/success_page/')
    else:
        form = JobForm(instance=job)

    return render(request, 'webapp/job_update.html', {'form': form})


def success_page(request):
    return render(request, 'webapp/success_page.html')
