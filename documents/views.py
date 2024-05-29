from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.shortcuts import render, get_object_or_404, redirect

from documents.models import Document
from employees.models import Employee
from django.contrib import messages


# Create your views here.


@login_required(login_url='login')
def index(request):
    if 'term' in request.GET:
        documents = Document.objects.filter(title__icontains=request.GET.get('term'))
        return render(request, 'documents/documents.html', {'documents': documents})
    documents = Document.objects
    return render(request, 'documents/documents.html', {'documents': documents})


@login_required(login_url='login')
def add_document(request):
    uploads_count = request.session.get('uploads_count', 0)
    employees = Employee.objects.all()
    documents = Document.objects.all()[:uploads_count]
    if request.method == 'POST':
        if request.POST['title'] and 'file' in request.FILES:
            document = Document()
            document.title = request.POST.get('title')
            document.file = request.FILES.get('file')
            if request.POST['employee']:
                document.employee = get_object_or_404(Employee, pk=request.POST.get('employee'))
                document.is_general = False
            document.save()
            uploads_count += 1
            request.session['uploads_count'] = uploads_count
            return redirect('add_document')
        else:
            form_data = request.POST.copy()
            if request.POST['employee']:
                form_data['employee'] = int(request.POST.get('employee'))
            return render(request, 'documents/add_document.html', {'employees': employees, 'documents': documents, 'error': 'Title and file required!', 'form_data': form_data})
    else:
        return render(request, 'documents/add_document.html', {'employees': employees, 'documents': documents})


@login_required(login_url='login')
def edit_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    employees = Employee.objects.all()
    if request.method == 'POST':
        if request.POST['title']:
            document.title = request.POST.get('title')
        else:
            return render('documents/edit_document.html', {'error': 'Title is required!'})
        if 'file' in request.FILES:
            document.file = request.FILES.get('file')
        if request.POST['employee']:
            employee = get_object_or_404(Employee, pk=request.POST.get('employee'))
            document.employee = employee
            document.is_general = False
        document.save()
        return redirect('/documents/')
    else:
        return render(request, 'documents/edit_document.html', {'document': document, 'employees': employees})


@login_required(login_url='login')
def delete_document(request, pk):
    document = Document.objects.get(pk=pk)
    document.delete()
    return redirect('/documents/')

