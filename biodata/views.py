import csv, io
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib import messages
# from django.contrib.auth.decorators import permission_required



from .models import *
from .forms import EmployeeForm

# Create your views here.
def index(request):
    return render(request, 'test_app/index.html')

def preview(request):
    details = Employee.objects.all()
    context = {
        'details': details
    }
    return render(request, 'test_app/preview.html', context)

def  history(request):
    return redirect('/admin/')



def add_detail(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/preview')

    else:
        form = EmployeeForm
        return render(request, 'test_app/add_detail.html', {'form':form})

def edit_detail(request, pk):
    detail = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance = detail)
        if form.is_valid():
            form.save()
            return redirect('/preview')
    else:
        form = EmployeeForm(instance = detail)

        return render(request, 'test_app/edit_detail.html', {'form':form})

def delete_detail(request, pk):
    Employee.objects.filter(id=pk).delete()
    details = Employee.objects.all()
    context = {
        'details':details
    }
    return render(request, 'test_app/preview.html', context)


# @permission_required('admin.can_add_log_entry')
def upload_detail(request):
    if request.method == 'GET':
        return render(request, 'test_app/upload_detail.html')
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file, please upload a csv file.')
    
    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set) # Putting it in a stream
    next(io_string)

    for column in csv.reader(io_string, delimiter = ',', quotechar = '|'):
        # _, allows us to skip the .save() call
        _, created = Employee.objects.update_or_create(
            firstname = column[0],
            lastname = column[1],
            age = column[2],
            gender = column[3],
            address = column[4],
            date_of_birth = column[5],
            email = column[6]
        )
        context = {}
        return render(request, 'test_app/preview.html', context, prompt)