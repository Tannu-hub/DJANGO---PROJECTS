from django.contrib import admin
from myapp.models import EmpoloyeeModel
from myapp.models import StudentModel

# Register your models here.



class StudentModelAdmin(admin.ModelAdmin):
    admin.site.register(StudentModel)



class EmpoloyeeModelAdmin(admin.ModelAdmin):
    list_display = ['Emp_name','Emp_id', 'Dpt_no', 'is_active']

admin.site.register(EmpoloyeeModel , EmpoloyeeModelAdmin)


