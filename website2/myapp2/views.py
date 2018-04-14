from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def disp(request):
    return HttpResponse('<h1> WELCOME TO BVRIT COLLEGE </h1>')
    return render(request,'myapp2/home1.html')

