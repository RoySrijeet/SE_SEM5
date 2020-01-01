from django.contrib import admin
from customer.models import Caterer
from customer.models import Decorator
from customer.models import Hall
from customer.models import PayMod
from customer.models import Studio
from customer.models import EventDetails
from customer.models import Customer
from customer.models import Planner

# Register your models here.
admin.site.register(Caterer)
admin.site.register(Customer)
admin.site.register(Hall)
admin.site.register(EventDetails)
admin.site.register(Decorator)
admin.site.register(PayMod)
admin.site.register(Planner)
admin.site.register(Studio)


