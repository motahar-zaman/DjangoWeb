from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name' : 'Fariya'})

def add(request):
    no1 = int(request.POST['num1'])
    no2 = int(request.POST['num2'])
    res = no1 + no2
    return render(request, 'result.html', {'result' : res})