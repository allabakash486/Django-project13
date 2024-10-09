from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(Employees)
admin.site.register(Dept)
