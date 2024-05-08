from django.urls import path
from . import views

urlpatterns = [
    path('',views.allemployees,name='allemployees'),
     path('employee/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),
]
