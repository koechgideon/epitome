from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')

def login(request):
    return render(request, 'app/login.html')

def register(request):
    return render(request, 'app/register.html')
