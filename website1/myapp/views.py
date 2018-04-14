from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def disp(request):
    return render(request,'myapp/home.html')
    #return HttpResponse('<h1>welcome to django appln</h1>')