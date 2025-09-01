# Employee Management API

A **Django REST Framework (DRF)** project for managing synthetic employee data with **JWT authentication**, **PostgreSQL (Neon)**, and **API documentation via Swagger**.  
This project demonstrates **data modeling, API development, JWT authentication, and analytics integration**.

---

## Features
- Employee CRUD API with DRF  
- JWT Authentication (access & refresh tokens)  
- PostgreSQL (Neon) cloud database integration  
- Swagger/OpenAPI documentation via `drf-yasg`  
- Rate limiting / throttling for APIs  
- Fake employee data generation using Faker  
- Analytics-ready APIs (salary distribution, performance)  
- Clean, extensible structure for future apps  

---

## Project Structure
employee_project/
│── employee_project/ # Project settings & URLs
│── employees/ # App with models, views, serializers, urls
│── manage.py
│── venv/ # Virtual environment (not committed)
│── requirements.txt
│── README.md
│── .env # Environment variables (DB connection, secret keys)


---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/employee_project.git
cd employee_project

python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows

pip install -r requirements.txt

SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=postgresql://<username>:<password>@<host>/<dbname>?sslmode=require

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

POST /api/token/
{
    "username": "your_username",
    "password": "your_password"
}

POST /api/token/refresh/
Authorization: Bearer <your_token>

API Endpoints
Endpoint	Method	Auth Required	Description
/admin/	GET	✅	Django admin panel
/api/	GET	❌	API root (DRF router)
/api/employees/	GET	✅	List all employees
/api/employees/	POST	✅	Create new employee
/api/employees/{id}/	GET	✅	Retrieve employee by ID
/api/employees/{id}/	PUT	✅	Update employee
/api/employees/{id}/	DELETE	✅	Delete employee
/api/token/	POST	❌	Obtain JWT token
/api/token/refresh/	POST	❌	Refresh JWT token
/swagger/	GET	❌	API documentation (Swagger UI)

python manage.py shell
from employees.models import Employee
from faker import Faker
import random

faker = Faker()

for _ in range(10):
    Employee.objects.create(
        name=faker.name(),
        email=faker.email(),
        department=random.choice(["HR", "IT", "Finance", "Marketing"]),
        salary=random.randint(40000, 120000),
        join_date=faker.date_this_decade()
    )


ere are all the URL endpoints (links) for your project:
Admin
http://127.0.0.1:8000/admin/
JWT Authentication
Obtain token: http://127.0.0.1:8000/api/token/
Refresh token: http://127.0.0.1:8000/api/token/refresh/
Employees API
API Root: http://127.0.0.1:8000/api/
List employees: http://127.0.0.1:8000/api/employees/
Retrieve/update/delete employee: http://127.0.0.1:8000/api/employees/{id}/
Analytics / Charts (if implemented)
Salary chart: http://127.0.0.1:8000/api/employees/salary-chart/
Swagger / API Documentation
Swagger UI: http://127.0.0.1:8000/swagger/
