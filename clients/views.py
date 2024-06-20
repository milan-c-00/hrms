from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect,render
from .models import Client
from .forms import ClientForm
from .models import Employee
from django.db.models import Q



def allclients(request):
    query = request.GET.get('q')
    if query:
        clients = Client.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(professional_email__icontains=query) |
            Q(employee__first_name__icontains=query) |
            Q(employee__last_name__icontains=query) |
            Q(employee__title__icontains=query)
        ).select_related('employee')
    else:
        clients = Client.objects.select_related('employee').all()

    context = {
        'clients': clients,
    }

    return render(request, 'clients/allclients.html', context)



def create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            if 'image' in request.FILES:
                form.save()
            else:
                form.instance.image = None
                form.save()
            return redirect('/clients/') 
    else:
        form = ClientForm()
    return render(request, 'clients/create.html', {'form': form})



def detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/clients/')
    else:
        form = ClientForm(instance=client)

    return render(request, 'clients/detail.html', {'client': client, 'form': form})






    