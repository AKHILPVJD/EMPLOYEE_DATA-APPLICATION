from django.shortcuts import render
from django.shortcuts import redirect

from .models import Employee


# Create your views here.
def create_employee(request):    #4
    if request.method == 'POST':
        name = request.POST['name']
        designation = request.POST['designation']
        email = request.POST['email']
        phone = request.POST['phone']
        
        employee = Employee(name=name, designation=designation, email=email,phone=phone)
        employee.save()
        return redirect('list_employee')
    return render(request, 'create_employee.html')

def list_employee(request):          #2
    employees = Employee.objects.all()
    return render(request, 'list_employee.html', {'employees': employees})
    
def update_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    
    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.designation = request.POST['designation']
        employee.email = request.POST['email']
        employee.phone = request.POST['phone']
        employee.save()
        return redirect('list_employee')
    
    return render(request, 'update_employee.html', {'employee': employee})

def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    return redirect('list_employee')
    
    


    
    
    