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

def detail(request, employee_id):
    detailemployee=get_object_or_404(Employee, pk=employee_id)
    return render(request,'employees/detail.html',{'employee':detailemployee})

def personal(request, employee_id):
    personalemployee=get_object_or_404(Employee, pk=employee_id)
    return render(request,'employees/personal.html',{'personalemployee':personalemployee})

def education(request, employee_id):
    employee=get_object_or_404(Employee, pk=employee_id)
    return render(request,'employees/education.html',{'employee':employee})

def jobobjective(request, employee_id):
    employee=get_object_or_404(Employee, pk=employee_id)
    return render(request,'employees/jobobjective.html',{'employee':employee})

def documents(request, employee_id):
  #  documents=get_object_or_404(Employee, pk=employee_id)
    return render(request,'employees/documents.html')

def status(request, employee_id):
    employee=get_object_or_404(Employee, pk=employee_id)
    return render(request,'employees/status.html',{'employee':employee})

def jobdetails(request, employee_id):
  #  documents=get_object_or_404(Employee, pk=employee_id)
    return render(request,'employees/jobdetails.html')

def performance(request, employee_id):
  #  documents=get_object_or_404(Employee, pk=employee_id)
    return render(request,'employees/performance.html')

def daysoff(request, employee_id):
  #  documents=get_object_or_404(Employee, pk=employee_id)
    return render(request,'employees/daysoff.html')


