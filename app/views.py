from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_Dept(request):
    Dno = int(input("Enter the Department number"))
    Dn = input('Enter the deotartment name')
    Dl = input("Enter the location")
    # DO =Dept.objects.get_or_create(Deptno =Dno,Dept_name = Dn,Dept_loc=Dl)
    # if DO[1]:
    #     return HttpResponse("Department   is created sucessfully......!")
    # else:
    #     return HttpResponse(" Department is Already exists .....!")
    # DO = Dept.objects.get(Deptno = Dno)
    # if DO:
    #     return HttpResponse("Department is fetched sucessfully....!")
def empdetails(request):
    empdo = Employees.objects.all()
    d={'empdo':empdo}
    return render(request,'empdetails.htm',d)
    

    