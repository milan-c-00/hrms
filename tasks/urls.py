from django.urls import path
from . import views

urlpatterns = [
     path('',views.alltasks,name='alltasks'),
     path('create/', views.create, name='create'),
     

   
]
