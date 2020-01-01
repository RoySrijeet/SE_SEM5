from django.shortcuts import render
from django.http import HttpResponse
#from  django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#from .forms import UserRegisterForm
# Create your views here.
from django.template import RequestContext
#from django.core.context_processors import csrf
from customer.forms import Customer as RegisForm
from customer.models import Customer as Regis
from customer.forms import EventDetails as Ed1
from customer.models import EventDetails as Ed2

#def customer(request):
#    return render(request, 'customer.html', {'name': 'Srijeet'})

# def add(request):
#     a = int(request.POST['num1'])
#     b = int(request.POST['num2'])
#     sum = a + b
#     return render(request, 'result.html', {'result': sum})
def register(request):
    if request.method=='POST':
        form=RegisForm(request.POST)
        if form.is_valid():
            f_name = request.POST.get('f_name', '')
            l_name = request.POST.get('l_name', '')
            organisation = request.POST.get('organisation', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            phone = request.POST.get('phone', '')
            regis_obj=Regis(f_name =f_name ,l_name =l_name ,organisation =organisation ,email =email ,password =password ,phone = phone )
            regis_obj.save()
            #return HttpResponseRedirect(reverse('customer:register'))
    else:
        form=RegisForm()

    return render(request, 'register.html',{'form':form,}, RequestContext(request))

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

def submit_details(request):
    if request.method == 'POST':
        form = Ed1(request.POST)
        if form.is_valid():
            email_id = request.POST.get['email_id']

            date = request.POST.get['date']
            time = request.POST.get['time']
            cus_id = request.POST.get['cus_id']
            hall_id = request.POST.get['hall_id']
            studio_id = request.POST.get['studio_id']

            caterer_id = request.POST.get['caterer_id']

            decor_id = request.POST.get['decor_id']
            planner_id = request.POST.get['planner_id']
            regis_obj = Ed2(email_id=email_id,date=date,  time=time,cus_id=cus_id,  hall_id=hall_id,studio_id = studio_id,caterer_id=caterer_id,decor_id=decor_id,planner_id=planner_id)
            regis_obj.save()
            # return HttpResponseRedirect(reverse('customer:register'))
            #return HttpResponseRedirect('/success/')
    else:
        form = Ed1()

    return render(request, 'submit_details.html', {'form': form, },RequestContext(request))

  #  return render(request,'submit_details.html',RequestContext(request))
'''
def submit_details(request):
    if request.method == 'POST':
        if request.POST.get('email_id') and request.POST.get('date'):
            post = EventDeatails()
            post.title = request.POST.get('email_id')
            post.content = request.POST.get('date')
            post.save()

            return render(request, 'submit_details.html', {'form': form, }, RequestContext(request))

    else:
        return render('submit_details.html', {'form': form, }, RequestContext(request))


'''