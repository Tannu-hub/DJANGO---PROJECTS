from django.shortcuts import render
from myapp.models import EmployeeModel
from django.

# Create your views here.

def empoloyee_view(request):
     all_data = EmployeeModel.objects.all()
     return render(request,'all_data.html',{"all_data": all_data})

def filterd_data(request):
    all_data = EmployeeModel.objects.filter(salaray = 4000)
    all_data = EmployeeModel.objects.filter(salaray__gt= 6500)
    all_data = EmployeeModel.objects.filter(salaray__gt= 6500)
    all_data = EmployeeModel.objects.filter(salaray__gt= 6500)
    all_data = EmployeeModel.objects.filter(salaray__gt= 6500)
    all_data = EmployeeModel.objects.filter(salaray__gt= 6500)
    all_data = EmployeeModel.objects.filter(salaray__gt= 6500)
    all_data = EmployeeModel.objects.filter(salaray__gt= 6500)

    all_data = EmployeeModel.objects.filter(salaray__gt= 6500)

    all_data = EmployeeModel.objects.filter(salaray__gt= 6500)

    
    all_data = EmployeeModel.objects.filter(Q(id_range = [10,20]) |
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            )
    return render(request,'filtered_data.html')



