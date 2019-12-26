from django.db import models
#RAW SKELETON FROM DATA DICTIONARY
#NO RELATIONS ESTABLISHED
# Create your models here.
class Caterer(models.Model):
    cat_id  = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20)
    location = models.CharField(max_length = 20)
    manager_id = models.AutoField(primary_key = False)
    #manager_id = models.InteherField(max_length=10)
    cost_p = models.FloatField(null=True)
    rating = models.FloatField(null = True)

class Decorator(models.Model):
    dec_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=20)
    ofc_address = models.CharField(max_length=20)
    manager_id = models.AutoField(primary_key=False)
    avg_rate = models.FloatField(null=True)
    rating = models.FloatField(null=True)

class Hall(models.Model):
    hall_id = models.AutoField(primary_key  = True)
    name =  models.CharField(max_length = 20 )
    location = models.CharField(max_length = 20 )
    area = models.FloatField()
    capacity = models.IntegerField()
    manager_id= models.AutoField(primary_key=False)
    rent = models.FloatField(null=True)
    rating = models.FloatField(null=True)

class Studio(models.Model):
    st_id = models.AutoField(primary_key  = True)
    name = models.CharField(max_length=20)
    st_addr = models.CharField(max_length=20)
    manager_id = models.AutoField(primary_key=False)
    avg_rate = models.FloatField(null=True)
    rating = models.FloatField(null=True)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    acc_type = models.IntegerField()
    email = models.CharField(max_length=20)
    city = models.CharField(max_length=10,null = True)
    phone = models.CharField(max_length=10,null = True)

class AccType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=10)

class LoginInfo(models.Model):
    user_id = models.IntegerField(primary_key=True)
    ip_addr = models.CharField(max_length= 10)
 #   login_time =
  #  logout_time =

class EventDetails(models.Model):
    event_id = models.AutoField(primary_key=True)
    cus_id =models.IntegerField()
    #date
    hall_id = models.IntegerField(null=True)
    studio_id = models.IntegerField(null=True)
    caterer_id = models.IntegerField(null=True)
    decor_id = models.IntegerField(null=True)
    planner_id = models.IntegerField(null=True)

class PlanEvent(models.Model):
    event_id = models.IntegerField(primary_key=True)
    planner_id = models.IntegerField(primary_key=True)
    manager_id = models.IntegerField(primary_key=True)

class CustomerBill(models.Model):
    bill_no = models.AutoField(primary_key=True)
    event_id = models.IntegerField()
    hall_charge = models.FloatField(null=True)
    studio_charge = models.FloatField(null=True)
    caterer_charge = models.FloatField(null=True)
    decor_charge = models.FloatField(null=True)
    planner_charge = models.FloatField(null=True)
    total_charge = models.FloatField()
    paid = models.FloatField(null=True)
    #latepayday
    amount_due = models.FloatField(null=True)
    mode_of_pay = models.IntegerField(null=True)

class VendorBill(models.Model):
    event_id = models.IntegerField(primary_key=True)
    vendor_id = models.IntegerField(primary_key=True)
    amount = models.FloatField()
    paid = models.FloatField()
    #lstpayday
    due = models.FloatField(null=True)
    mode =models.IntegerField(null=True)

class PayMod(models.Model):
    pay_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    bank = models.CharField(max_length=20,null =True)
    upi = models.CharField(max_length=20,null =True)


