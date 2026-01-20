from django.shortcuts import render
from myapp.models import EmpoloyeeModel

# Create your views here.

def Empolyee_view(request):
    all_data = EmpoloyeeModel.objects.all()     # to fetch all teh data from db
    context = {"Emopolyee_data": all_data}
    return render(request, 'Empoloyee.html',context)

