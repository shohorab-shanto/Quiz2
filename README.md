Employee Management API
A Django REST Framework (DRF) project for managing synthetic employee data with JWT authentication, PostgreSQL (Neon), and API documentation via Swagger.
The project demonstrates data modeling, API development, JWT authentication, and analytics integration.
Features
Employee CRUD API with DRF.
JWT Authentication (access & refresh tokens).
PostgreSQL (Neon) database integration.
Swagger/OpenAPI documentation.
Rate limiting / throttling for APIs.
Fake employee data generation using Faker.
Analytics-ready APIs (salary distribution, performance).
Clean, extensible structure for future apps.
Project Structure
employee_project/
│── employee_project/ # Project settings & URLs
│── employees/ # App with models, views, serializers, urls
│── manage.py
│── venv/ # Virtual environment (not committed)
│── requirements.txt
│── README.md
│── .env # Environment variables (DB connection, secret keys)
Installation
Clone the Repository
git clone https://github.com/your-username/employee_project.git
cd employee_project
Setup Virtual Environment
python -m venv venv
source venv/bin/activate # Mac/Linux
venv\Scripts\activate # Windows
Install Dependencies
pip install -r requirements.txt
Setup Environment Variables
Create a .env file in the project root:
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=postgresql://<username>:<password>@<host>/<dbname>?sslmode=require
Apply Migrations
python manage.py migrate
Create Superuser (for Django Admin)
python manage.py createsuperuser
Run Server
python manage.py runserver
Authentication
This project uses JWT via djangorestframework-simplejwt.
Obtain token:
POST /api/token/
{
"username": "your_username",
"password": "your_password"
}
Refresh token:
POST /api/token/refresh/
Use the returned access token in headers for protected endpoints:
Authorization: Bearer <your_token>
API Endpoints
Endpoint	Method	Auth Required	Description
/admin/	GET	Yes	Django admin panel
/api/	GET	No	API root (DRF router)
/api/employees/	GET	Yes	List all employees
/api/employees/	POST	Yes	Create new employee
/api/employees/{id}/	GET	Yes	Retrieve employee by ID
/api/employees/{id}/	PUT	Yes	Update employee
/api/employees/{id}/	DELETE	Yes	Delete employee
/api/token/	POST	No	Obtain JWT token
/api/token/refresh/	POST	No	Refresh JWT token
/swagger/	GET	No	API documentation (Swagger UI)
Fake Data Generation
You can populate the database with fake employees using Django shell:
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
Future Improvements
Add Plotly/Chart.js visualizations for analytics.
Add Attendance & Performance models.
Deploy with Docker + Render/Heroku.
Tech Stack
Backend: Django, DRF
Auth: JWT (SimpleJWT)
Database: PostgreSQL (Neon)
Docs: drf-yasg (Swagger UI)
Fake Data: Faker
Author
Shohorab Shanto
Software Engineer — Building AI & Web solutions