from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('login.html', views.login, name='login'),
    path('wedding.html', views.wedding, name='wedding'),
    path('birthday.html', views.birthday, name='birthday'),
    path('anniversary.html', views.anniversary, name='anniversary'),
    path('corporate.html', views.corporate, name='corporate'),
    path('cultural.html', views.cultural, name='cultural'),
    path('customize.html', views.customize, name='customize'),
    path('register.html', views.register, name='register'),
    path('submit_details.html',views.submit_details,name='submit_details')
]
