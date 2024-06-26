from django.urls import path

from documents import views

urlpatterns = [
    path('', views.index, name='documents'),
    path('add/', views.add_document, name='add_document'),
    path('edit/<int:pk>/', views.edit_document, name='edit_document'),
    path('delete/<int:pk>/', views.delete_document, name='delete_document'),
]
