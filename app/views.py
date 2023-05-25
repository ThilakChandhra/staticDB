from django.shortcuts import render

# Create your views here.

from app.models import *

def sample(request):
    LOD=Department.objects.all()
    d={'dept':LOD}
    return render(request,'sample.html',d)

def sample1(request):
    LOE=Employee.objects.all()
    d={'emp':LOE}
    return render(request,'sample1.html',d)
