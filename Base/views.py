from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def experience(request):
    return render(request, 'experience.html')

def projects(request):
    return render(request, 'projects.html')

def skills(request):
    return render(request, 'skills.html')

def Education(request):
    return render(request, 'Education.html')