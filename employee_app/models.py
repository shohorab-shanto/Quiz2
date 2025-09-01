from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    date_joined = models.DateField()
    salary = models.FloatField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present','Present'),('Absent','Absent')])
    hours_worked = models.FloatField()

    def __str__(self):
        return f"{self.employee} - {self.date}"

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performances')
    review_date = models.DateField()
    rating = models.IntegerField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.employee} - {self.review_date}"
