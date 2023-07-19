from django.contrib import admin
from .models import Medication 
from .models import Database

admin.site.register(Medication) 
admin.site.register(Database)
