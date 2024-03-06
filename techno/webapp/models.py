from django.db import models


# Employee Table
class Employee(models.Model):
    emp_ssn = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    address = models.TextField()
    emp_efficiency = models.FloatField()

    def __str__(self):
        return f"Details Of {self.emp_name}"


# Job Table
class Job(models.Model):
    job_id = models.IntegerField(primary_key=True, default=0)
    job_name = models.CharField(max_length=100)
    tool_code = models.ForeignKey('Tool', on_delete=models.CASCADE, db_column='tool_code', to_field='tool_code')
    length = models.FloatField()
    no_of_holes = models.IntegerField()


# Machine Table
class Machine(models.Model):
    machine_name = models.CharField(max_length=100, primary_key=True)
    job_name = models.ForeignKey(Job, on_delete=models.CASCADE, db_column='job_name', default='default_job_name')

    class Meta:
        unique_together = ('machine_name', 'job_name')


# Performs Table
class Performs(models.Model):
    date = models.DateField(primary_key=True)
    emp_ssn = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_ssn')
    job_name = models.ForeignKey(Job, on_delete=models.CASCADE, db_column='job_name')
    machine_name = models.ForeignKey(Machine, on_delete=models.CASCADE)
    shift_number = models.IntegerField()
    shift_duration = models.FloatField()
    achieved = models.IntegerField()
    partial_shift = models.IntegerField()
    target = models.IntegerField()

    class Meta:
        unique_together = ['date', 'emp_ssn', 'job_name']


# Tool Table
class Tool(models.Model):
    tool_code = models.CharField(primary_key=True, max_length=100)
    tool_name = models.CharField(max_length=100)
    max_length = models.FloatField()
    cost = models.FloatField()
    length_cut = models.FloatField()
    no_of_brk_points = models.IntegerField()
    tool_efficiency = models.FloatField()


