from django.urls import path
from . import views

urlpatterns = [
     path('',views.allclients,name='allclients'),
     path('create/', views.create, name='create'),
     path('<int:client_id>/', views.detail, name='detail')

     

   
]
