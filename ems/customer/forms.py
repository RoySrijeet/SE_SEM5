import django.forms as forms

from django.utils import timezone
#RAW SKELETON FROM DATA DICTIONARY
#NO RELATIONS ESTABLISHED
# Create your models here.
class Customer(forms.Form):
    #user_id = forms.AutoField(primary_key=True)
    f_name = forms.CharField(max_length=20)
    l_name = forms.CharField(max_length=20)
    organisation = forms.CharField(max_length=10)
    email = forms.EmailField()
    password = forms.CharField(max_length=15)
    phone = forms.CharField(max_length=10)

class EventDetails(forms.Form):
   #event_id = forms.AutoField(primary_key=True)
    email_id = forms.CharField(max_length=20)
    date = forms.CharField(max_length=20)
    time = forms.CharField(max_length=5)
    cus_id = forms.CharField(max_length=20)
    hall_id = forms.CharField(max_length=20)
    studio_id = forms.CharField(max_length=20)
    caterer_id = forms.CharField(max_length=20)
    decor_id = forms.CharField(max_length=20)
    planner_id = forms.CharField(max_length=20)
  #  total=forms.FloatField(null=True)

class PayMod(forms.Form):
    card_number = forms.CharField(max_length = 20)
    expiration_date = forms.DateField()
    cv_code = forms.IntegerField()
    card_owner = forms.CharField(max_length=20)
'''

class EventDetails(forms.Form):
   # event_id = forms.AutoField(primary_key=True)
    email_id = forms.CharField(max_length=20)
    date = forms.CharField(max_length=20)
'''