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
    title=forms.CharField(label="Task Name")
    status = forms.ChoiceField(choices=STATUS_CHOICES, label='Status')
    importance = forms.ChoiceField(choices=IMPORTANCE_CHOICES, label='Importance')
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), label='Employee')
    start = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = ['title', 'status', 'start', 'end', 'employee', 'importance']
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        status = cleaned_data.get("status")
        start = cleaned_data.get("start")
        end = cleaned_data.get("end")
        employee = cleaned_data.get("employee")
        importance = cleaned_data.get("importance")


        if not title:
            self.add_error('title', 'This field is required.')
        if not status:
            self.add_error('status', 'This field is required.')
        if not start:
            self.add_error('start', 'This field is required.')
        if not end:
            self.add_error('end', 'This field is required.')
        if not employee:
            self.add_error('employee', 'This field is required.')
        if not importance:
            self.add_error('importance', 'This field is required.')


        return cleaned_data