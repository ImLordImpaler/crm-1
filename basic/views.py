from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Enquiry , Product , Employee
from .forms import ProductForm , EnquiryForm , EmployeForm
# Create your views here.

def home(request):
    enq = Enquiry.objects.all()
    
    pro = Product.objects.all().order_by('quantity')
   
    params = {
        'enq': enq ,
        'pro' : pro
    }
    return render(request , 'basic/dashboard.html' , params)



def enquiry(request):
    enq = Enquiry.objects.all()
    form = EnquiryForm()
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else :
            return HttpResponse('<h3> Try again </h3>')
    else :
        form = EnquiryForm()
    params = {
        'form' : form ,
        'pro' : enq
    }

    return render(request , 'basic/enquiry.html' , params)

def enquiryUpdate(request , pk):
    enq = Enquiry.objects.get(id = pk)
    
    if request.method == 'POST':
        form = EnquiryForm(request.POST , instance=enq)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse('not found')
    else:
        form = EnquiryForm(instance= enq)
    params = {
        'form' : form
    }
    return render(request , 'basic/enquiryForm.html' , params)



def product(request):
    enq = Product.objects.all()
    form = EnquiryForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else :
            return HttpResponse('<h3> Try again </h3>')
    else :
        form = ProductForm()
    params = {
        'form' : form ,
        'pro' : enq
    }

    return render(request , 'basic/product.html' , params)
    


def productEnquiry(request , pk):
    enq = Product.objects.get(id = pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST , instance=enq)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse('not found')
    else:
        form = ProductForm(instance= enq)
    params = {
        'form' : form
    }
    return render(request , 'basic/productForm.html' , params)

def employee(request):
    emp = Employee.objects.all()
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else :
            return HttpResponse('kya hai reh halkat. Tereko likhne ka nai atta kya?')
    else:
        form = EmployeForm()
    params = {
        'form': form,
        'pro': emp
    }
    return render(request , 'basic/employee.html' , params)

def employeeUpdate(request , pk):
    enq = Employee.objects.get(id = pk)
    
    if request.method == 'POST':
        form = EmployeForm(request.POST , instance=enq)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return HttpResponse('not found')
    else:
        form = EmployeForm(instance= enq)
    params = {
        'form' : form
    }
    return render(request , 'basic/empForm.html' , params)

def stock(request):
    pro = Product.objects.all()
    params = {
        'stock': pro
    }
    return render(request , 'basic/album.html' , params)

def clients(request):
    params = {

    }
    return render(request , 'basic/clients.html' , params)

def deleteEmployee(request , pk):
    Emp = Employee.objects.get(id=pk)
    if request.method == 'POST':
        Emp.delete()
        return redirect('employee')
       
    
    params = {
        'item': Emp
    }

    return render(request, 'basic/deleteEmployee.html' , params)

def deleteProduct(request , pk):
    pro = Product.objects.get(id=pk)
    if request.method=='POST':
        pro.delete()
        return redirect('product')
    params = {
        'item': pro
    }
    return render(request , 'basic/deleteProduct.html' , params)

def deleteEnquiry(request , pk):
    pro = Enquiry.objects.get(id=pk)
    if request.method=='POST':
        pro.delete()
        return redirect('enquiry')
    params = {
        'item': pro
    }
    return render(request , 'basic/deleteEnquiry.html' , params)