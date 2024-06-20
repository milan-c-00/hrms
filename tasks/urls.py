from django.urls import path
from . import views

urlpatterns = [
     path('',views.alltasks,name='alltasks'),
     path('add/', views.add, name='add'),
     path('<int:task_id>/', views.taskdetail, name='taskdetail'),
]
