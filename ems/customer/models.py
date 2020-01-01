from django.db import models
from django.utils import timezone
#RAW SKELETON FROM DATA DICTIONARY
#NO RELATIONS ESTABLISHED
# Create your models here.

class Caterer(models.Model):
    cat_id  = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20)
    cost_p = models.FloatField()
    rating = models.FloatField(null = True)
    experience=models.TextField()

class Decorator(models.Model):
    dec_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=20)
    cost_p = models.FloatField()
    rating = models.FloatField(null=True)
    experience = models.TextField()

class Hall(models.Model):
    hall_id = models.AutoField(primary_key  = True)
    name =  models.CharField(max_length = 20 )
    location = models.CharField(max_length = 20 )
    capacity = models.IntegerField()
    cost_p = models.FloatField()
    rating = models.FloatField(null=True)
    experience = models.TextField()

class Studio(models.Model):
    st_id = models.AutoField(primary_key  = True)
    name = models.CharField(max_length=20)
    cost_p = models.FloatField()
    rating = models.FloatField(null=True)
    experience = models.TextField()

class Customer(models.Model):
   # user_id = models.AutoField(primary_key=True)
    user_id = models.CharField(primary_key=True,max_length = 100)

    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    organisation = models.CharField(max_length=10, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=15,default = 'son')
    phone = models.CharField(max_length=10)

class Planner(models.Model):
    planner_id= models.AutoField(primary_key=True)
    plan_brand= models.CharField(max_length=20)
    plan_name= models.CharField(max_length=20)
    message= models.TextField()

'''
class EventDetails(models.Model):
    event_id = models.AutoField(primary_key=True)
    cus_id = models.ForeignKey(Customer,on_delete = models.CASCADE)
    hall_id = models.ForeignKey(Hall,on_delete = models.CASCADE)
    studio_id = models.ForeignKey(Studio,on_delete = models.CASCADE)
    caterer_id = models.ForeignKey(Caterer,on_delete = models.CASCADE)
    decor_id = models.ForeignKey(Decorator,on_delete = models.CASCADE)
    planner_id = models.ForeignKey(Planner,on_delete = models.CASCADE)
    total=models.FloatField(null=True)
'''
class EventDetails(models.Model):
    email_id = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=5)
    event_id = models.CharField(primary_key=True,max_length = 20)
    cus_id = models.CharField(max_length = 20)
    hall_id = models.CharField(max_length = 20)
    studio_id = models.CharField(max_length = 20)
    caterer_id = models.CharField(max_length = 20)
    decor_id = models.CharField(max_length = 20)
    planner_id = models.CharField(max_length = 20)
    #total=models.FloatField(null=True)

class PayMod(models.Model):
    card_number = models.CharField(primary_key=True,max_length = 20)
    #expiration_date = models.DateTimeField()
    cv_code = models.IntegerField()
    card_owner = models.CharField(max_length=20)
'''
class EventDetails(models.Model):
    email_id = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
'''

