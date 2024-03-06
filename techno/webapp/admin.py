from django.contrib import admin
from .models import Employee, Job, Machine, Performs, Tool

admin.site.register(Employee)
admin.site.register(Job)
admin.site.register(Machine)
admin.site.register(Performs)
admin.site.register(Tool)
