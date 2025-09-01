from faker import Faker
import random
from datetime import date, timedelta
from .models import Employee, Attendance, Performance

fake = Faker()

def generate_employees(n=5):
    for _ in range(n):
        emp = Employee.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.unique.email(),
            department=random.choice(['HR','IT','Finance','Marketing']),
            date_joined=fake.date_between(start_date='-5y', end_date='today'),
            salary=random.randint(40000, 120000)
        )
        for i in range(30):
            day = date.today() - timedelta(days=i)
            Attendance.objects.create(
                employee=emp,
                date=day,
                status=random.choice(['Present','Absent']),
                hours_worked=random.randint(6,9)
            )
        for _ in range(3):
            Performance.objects.create(
                employee=emp,
                review_date=fake.date_between(emp.date_joined,'today'),
                rating=random.randint(1,5),
                comments=fake.sentence()
            )
