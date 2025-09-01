from rest_framework import routers
from django.urls import path
from .views import EmployeeViewSet, salary_chart

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = router.urls + [
    path('salary-chart/', salary_chart),
]
