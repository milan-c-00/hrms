from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Employee, Contract, Education, WorkExperience


def allemployees(request):
    if 'term' in request.GET:
        employees = Employee.objects.filter(name__icontains=request.GET.get('term'))
        return render(request, 'employees/allemployees.html', {'employees': employees})
    employees=Employee.objects
    return render(request,'employees/allemployees.html',{'employees':employees})

def all_performance(request):
    if 'term' in request.GET:
        employees = Employee.objects.filter(name__icontains=request.GET.get('term'))
        return render(request, 'employees/all_performance.html', {'employees': employees})
    employees=Employee.objects
    return render(request, 'employees/all_performance.html', {'employees':employees})

def interns(request):
    if 'term' in request.GET:
        employees = Employee.objects.filter(name__icontains=request.GET.get('term'))
        return render(request, 'employees/interns.html', {'employees': employees})
    employees = Employee.objects.filter(contract__internship=True).distinct()
    return render(request, 'employees/interns.html', {'employees':employees})

def add_employee(request):
    if request.method == 'POST':
        if request.POST['name'] and request.POST['birth_date'] and request.POST['position'] and request.POST['team']and request.POST['phone']:
            name = request.POST.get('name')
            birth_date = request.POST.get('birth_date')
            position = request.POST.get('position')
            team = request.POST.get('team')
            phone = request.POST.get('phone')
            personal_email = request.POST.get('personal_email')
            professional_email = request.POST.get('professional_email')
            city = request.POST.get('city')
            address = request.POST.get('address')
            image = request.FILES.get('image')

        # Create the Employee instance
            employee = Employee(
                name=name,
                birth_date=birth_date,
                position=position,
                team=team,
                phone=phone,
                personal_email=personal_email,
                professional_email=professional_email,
                city=city,
                address=address,
                image=image
            )
            employee.save()

            # Contract details
            emp_status = request.POST.get('status')
            internship_val = request.POST.get('internship')
            internship = internship_val == '1'
            print(internship)
            contract_start_date = request.POST.get('contract_start_date')
            contract_end_date = request.POST.get('contract_end_date')
            salary = request.POST.get('salary')

            # Create the Contract instance
            contract = Contract.objects.create(
                status=emp_status,
                internship=True if internship else False,
                start_date=contract_start_date,
                end_date=contract_end_date,
                salary=salary,
                employee=employee
            )

            contract.save()

            # Education details
            school = request.POST.get('school')
            school_location = request.POST.get('school_location')
            school_city = request.POST.get('school_city')
            degree = request.POST.get('degree')
            school_start_date = request.POST.get('school_start_date')
            school_end_date = request.POST.get('school_end_date')
            education_details = request.POST.get('education_details')

            # Create the Education instance
            emp_education = Education(
                employee=employee,
                school=school,
                location=school_location,
                city=school_city,
                degree=degree,
                start_date=school_start_date if school_start_date else None,
                end_date=school_end_date if school_end_date else None,
                details=education_details
            )
            emp_education.save()

            # Work experience details
            company = request.POST.get('company')
            company_location = request.POST.get('company_location')
            company_city = request.POST.get('company_city')
            work_position = request.POST.get('work_position')
            work_start_date = request.POST.get('work_start_date')
            work_end_date = request.POST.get('work_end_date')
            work_details = request.POST.get('work_details')

            # Create the WorkExperience instance
            work_experience = WorkExperience(
                employee=employee,
                company=company,
                location=company_location,
                city=company_city,
                position=work_position,
                start_date=work_start_date if work_start_date else None,
                end_date=work_end_date if work_end_date else None,
                details=work_details
            )
            work_experience.save()
            return redirect('allemployees')  # Redirect to employee list or some other page
        else:
            form_data = request.POST.copy()
            return render(request, 'employees/add_employee.html', {'form_data': form_data, 'error': 'Fill the required fields!'})

    return render(request, 'employees/add_employee.html')

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('/employees/')  
    return render(request, {'employee': employee})

def detail(request, employee_id):
    employee=get_object_or_404(Employee, pk=employee_id)
    return render(request,'employees/detail.html',{'employee':employee})

def personal(request, employee_id):
    employee=get_object_or_404(Employee, pk=employee_id)
    return render(request,'employees/personal.html',{'employee':employee})

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


