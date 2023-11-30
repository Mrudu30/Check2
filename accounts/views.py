from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . import models as m
from . import forms as f
from django.contrib import admin,messages
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.views.generic.detail import DetailView

# Create your views here.
@login_required(login_url='/login')
def student_add(request):
    form = f.studentform()
    if request.method == 'POST':
        form = f.studentform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('home')
        else:
            messages.error(request, 'there is some error please try again')
            
    context = {'form':form}
    return render(request,'form_render.html',context)

def home(request):
    return render(request,'home.html')   

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')       
        user = authenticate(request,username=username,password=password)
        if user !=None:
            login(request,user)
            return redirect(home)
        else:
            messages.error(request, "User name or pass do not exist")        
    context = {}
    return render(request,'login_register.html',context)     

# Showing all students
def show_students(request):
    q = request.GET.get('q') if request.GET.get('q')!= None else ''
    info = m.Student.objects.filter(
        Q(username__icontains=q) |
        Q(first_name__icontains=q)|
        Q(last_name__icontains=q)
    )
    context = {'info':info}
    return render(request,"students.html",context)

# details of a particular person
def details(request,pk):
    info = m.Student.objects.get(id=pk)
    context = {'info':info}
    return render(request,"details.html",context)

# edit details of the student
def edit_student(request,pk):
    Student = m.Student.objects.get(id=pk)
    form = f.edit_details(instance=Student)
    
    if request.method=='POST':
        form = f.edit_details(request.POST,instance=Student)
        if form.is_valid():
            form.save()
            return redirect('show_students')
        
    context = {'form':form,'Student':Student}
    return render(request,'form_render.html',context)

# showing parent detail
def parent_detail(request,pk):
    student = m.Student.objects.get(id=pk)
    context = {'student':student}
    return render(request,'parent_detail.html',context)

# edit parent deatails
def edit_parent(request,pk):
    student = m.Student.objects.get(id=pk)
    parent = student.parent
    form = f.parentform(instance=parent)
    
    if request.method=='POST':
        form = f.parentform(request.POST,instance=parent)
        if form.is_valid():
            form.save()
            return redirect('show_students')
        
    context = {'form':form,'parent':parent}
    return render(request,'form_render.html',context)

# adding exam details
def add_exam(request,pk):
        # Get the student object
    student = m.Student.objects.get(id=pk)
    