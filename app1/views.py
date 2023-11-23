from django.shortcuts import render

# Create your views here.

def conditions(request):
    d={'a':100}
    return render(request,'conditions.html',d)
