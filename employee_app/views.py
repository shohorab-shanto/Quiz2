from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from django.http import HttpResponse
import plotly.express as px
from .models import Employee
from .serializers import EmployeeSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Employee API!")


class EmployeeThrottle(UserRateThrottle):
    rate = '10/min'

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [EmployeeThrottle]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name','last_name','department','email']
    ordering_fields = ['salary','date_joined']

def home(request):
    return HttpResponse("Welcome to Employee API!")
def salary_chart(request):
    employees = Employee.objects.all()
    fig = px.bar(x=[e.first_name for e in employees],
                 y=[e.salary for e in employees],
                 title="Employee Salaries")
    return HttpResponse(fig.to_html())
