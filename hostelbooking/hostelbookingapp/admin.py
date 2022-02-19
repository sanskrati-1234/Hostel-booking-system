from django.contrib import admin
from .models import City,State,Hostel,Room,Tenant
# Register your models here.
admin.site.register(City)
admin.site.register(State)
admin.site.register(Hostel)
admin.site.register(Room)
admin.site.register(Tenant)