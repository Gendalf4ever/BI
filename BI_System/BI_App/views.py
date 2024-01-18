from django.shortcuts import render
from django.http import HttpResponse 

def home(request): 
    return render(request, 'BI_App/home.html')


def login(request):
    return render(request, 'BI_App/login.html')