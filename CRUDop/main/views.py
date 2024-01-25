from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import userDetail

# Create your views here.
def signup(request):
    user = None
    error_message = None
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        sig = userDetail(email=email,password=password)
        sig.save()
        return render(request,'signup.html',{'error':'User Created Successfully'})


        


    return render(request,'signup.html',{'user':user,'error_message':error_message})
def login_page(request):
    return render(request,'login.html')

def home_page(request):
    return render(request,'home.html')

def admin_page(request):
    
    adminU = userDetail.objects.all()
    

    return render(request,'admin.html',{'adminU':adminU})

def main_page(request):
    return render(request,'main.html')

def createUser(request):
    formPage = True
    return redirect(admin_page,{'formPage':formPage})