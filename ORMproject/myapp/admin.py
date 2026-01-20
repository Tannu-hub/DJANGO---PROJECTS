from django.contrib import admin
from myapp.models import EmpolyeeModel

# Register your models here.

class EmpolyeeModelAdmin(admin.ModelAdmin):
    list_display = ['E_name','Company','Jobrole','Sallary']




admin.site.register(EmpolyeeModel,EmpolyeeModelAdmin)

