from django import forms
from .models import Task, Employee

STATUS_CHOICES = [
    ('To Do', 'To Do'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
]

IMPORTANCE_CHOICES = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
]



class TaskForm(forms.ModelForm):
    status = forms.ChoiceField(choices=STATUS_CHOICES, label='Status')
    importance = forms.ChoiceField(choices=IMPORTANCE_CHOICES, label='Importance')
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), label='Employee')
    start = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={'class': 'form-control datepicker'}),
        label='Start Date'
    )
    end = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={'class': 'form-control datepicker'}),
        label='End Date'
    )

    class Meta:
        model = Task
        fields = ['title', 'status', 'start', 'end', 'employee', 'importance']
