from django.urls import path
from . import views

urlpatterns = [
    path('wedding-banquets.html', views.wedding_banquets, name='wedding-banquets'),
    path('wedding-caterers.html', views.wedding_caterers, name='wedding-caterers'),
    path('wedding-decorators.html', views.wedding_decorators, name='wedding-decorators'),
    path('wedding-photography.html', views.wedding_photography, name='wedding-photography'),
    path('wedding-beauticians.html', views.wedding_beauticians, name='wedding-beauticians'),
    path('wedding-planners.html', views.wedding_planners, name='wedding-planners')
]