from django.shortcuts import render
from django.http import HttpResponse

def disp(request):
    return render(request,'webapp/home.html')
    #return HttpResponse('<h1>Welcome to django</h1>')

# Create your views here.
