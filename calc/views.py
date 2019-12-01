from django.shortcuts import render
from django.http import HttpResponse
from . models import Destination, Employee, Position,kaam
from django.contrib.auth.models import User, auth
from .forms import EmployeeForm,kaamForm

# Create your views here.

def home(request):
   dest = Destination.objects.all()
   
   return render(request,'index.html',{'dest':dest})



def addtwonumber(request):
    num1 = int(request.POST['num1'])
    num2 =int( request.POST['num2'])
    result = num1+num2
    return render(request,'result.html',{'result':result})

def registration(request):

    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username = request.POST['username']
        email=request.POST['email']
        password= request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                print("lllll")
            elif User.objects.filter(email=email).exists():
                print(email)
            
            else:
                 user =User.objects.create_user(username=username,password=password1,email=email,last_name=last_name,first_name=first_name)
                 user.save()
    return render(request,'registration.html')




def login(request):
    if request.method == 'POST':
       username=request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username=username,password=password)

       if user is not None:
           auth.login(request,user)
           return redirect("/")

    else:
        return render(request,'login.html')





def employee_list(request):
    print('ssdfsdfsdf')
    return render(request,'addEmployee.html')


def employee_form(request):
     position = Position.objects.all()
     print("position",position)
     if request.method == "POST":  
        position = request.POST['position']
        print(position)
        print("2222222222222222222222")
        form = kaamForm(request.POST)  
        print("lobsang")
        if form.is_valid():  
            print("form is valid")
            try:  
                form.save() 
                print('save part')  
                return redirect('/show')  
            except:  
                print('ommmmmmm')
                pass 

        else:
            print("form is invalid") 
     else: 
        print("ommmm") 
        form = kaamForm()  
     return render(request,'addEmployee.html',{'form':form,'position':position})  


def show(request):  
    employees = kaam.objects.all()  
    return render(request,"show.html",{'employees':employees})  





def edit(request,id):
    employee = kaam.objects.get(id=id)
    return render(request,'edit.html', {'employee':employee}) 



def update(request,id):
    employee = kaam.object.get(id=id)
    form =kaamForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'edit.html',{'employee':employee})



def delete(request,id):
    employee = kaam.objects.get(id=id)
    employee.delete()
    return redirect('/show')