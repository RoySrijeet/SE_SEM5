from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def customer(request):
    return render(request, 'customer.html', {'name': 'Srijeet'})

# def add(request):
#     a = int(request.POST['num1'])
#     b = int(request.POST['num2'])
#     sum = a + b
#     return render(request, 'result.html', {'result': sum})

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def wedding(request):
    return render(request, 'wedding.html')

def birthday(request):
    return render(request, 'birthday.html')

def anniversary(request):
    return render(request, 'anniversary.html')

def corporate(request):
    return render(request, 'corporate.html')

def cultural(request):
    return render(request, 'cultural.html')

def customize(request):
    return render(request, 'customize.html')


