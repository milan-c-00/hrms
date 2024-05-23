from django.urls import path
from . import views

urlpatterns = [
    path('',views.allemployees,name='allemployees'),
     path('employee/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),
     path('<int:employee_id>/', views.detail,name='detail'),
     path('<int:employee_id>/personal', views.personal,name='personal'),
     path('<int:employee_id>/education', views.education,name='education'),
     path('<int:employee_id>/jobobjective', views.jobobjective,name='jobobjective'),
     path('<int:employee_id>/documents', views.documents,name='documents'),
     path('<int:employee_id>/status', views.status,name='status'),
     path('<int:employee_id>/jobdetails', views.jobdetails,name='jobdetails'),
     path('<int:employee_id>/performance', views.performance,name='performance'),
     path('<int:employee_id>/daysoff', views.daysoff,name='daysoff'),
]
