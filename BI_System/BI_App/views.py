from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
def home(request): 
    return render(request, 'BI_App/home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "login success")
            return redirect('BI_App/home.html')
        else:
            messages.warning(request, "error, please try again")
            return redirect('BI_App/login.html')

        # else:
            # return render(request, 'BI_App/login.html')
         
        
        
