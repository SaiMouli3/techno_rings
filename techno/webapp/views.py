from django.shortcuts import render, redirect
from .forms import EmployeeForm, ToolForm


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


def success_page(request):
    return render(request, 'webapp/success_page.html')
