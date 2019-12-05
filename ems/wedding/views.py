from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wedding_banquets(request):
    return render(request, 'wedding-banquets.html')

def wedding_caterers(request):
    return render(request, 'wedding-caterers.html')

def wedding_decorators(request):
    return render(request, 'wedding-decorators.html')

def wedding_photography(request):
    return render(request, 'wedding-photography.html')

def wedding_beauticians(request):
    return render(request, 'wedding-beauticians.html') 

def wedding_planners(request):
    return render(request, 'wedding-planners.html')