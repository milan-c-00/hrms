from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Employee

def allemployees(request):
    employees=Employee.objects
    return render(request,'employees/allemployees.html',{'employees':employees})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('/employees/')  
    return render(request, {'employee': employee})
