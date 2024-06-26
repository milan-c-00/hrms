from django.urls import path
from . import views

urlpatterns = [
    path('',views.allemployees,name='allemployees'),
    path('performance/',views.all_performance,name='all_performance'),
    path('interns/', views.interns, name='interns'),
    path('add/', views.add_employee, name='add_employee'),
     path('employee/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),
     path('<int:employee_id>/', views.detail,name='detail'),
     path('<int:employee_id>/personal', views.personal,name='personal'),
     path('<int:employee_id>/education', views.education,name='education'),
    path('<int:employee_id>/work_experience', views.work_experience, name='work_experience'),
     path('<int:employee_id>/jobobjective', views.jobobjective,name='jobobjective'),
     path('<int:employee_id>/documents', views.documents,name='documents'),
     path('<int:employee_id>/status', views.status,name='status'),
     path('<int:employee_id>/jobdetails', views.jobdetails,name='jobdetails'),
    path('<int:employee_id>/jobdetails/edit', views.edit_job_details, name='edit_job_details'),
     path('<int:employee_id>/performance', views.performance,name='performance'),
     path('<int:employee_id>/daysoff', views.daysoff,name='daysoff'),
    path('<int:employee_id>/performance/skills/add', views.add_skill, name='add_skill'),
    path('<int:employee_id>/performance/notes/add', views.add_note, name='add_note'),
    path('<int:employee_id>/performance/notes/<int:note_id>/delete', views.delete_note, name='delete_note'),
]
