from django.http import HttpResponse
from django.shortcuts import render
from information.models import Information
from organizations.models import Category
from jobs.models import Job

# Create your views here.

def show_home(request):
    categories = Category.objects.all() 
    job = Job.objects.all()
    return render(request, 'index.html', {'categories':categories, 'jobs':job})

def show_about(request): 
    # about = Information.objects.filter(section_id=1)
    about = Information.objects.filter(title='About us')
    return render(request, 'about.html', {'about':about})

def show_contacts(request):
    return render(request, 'contact.html')

def show_policies(request):
    return render(request, 'policy.html')
