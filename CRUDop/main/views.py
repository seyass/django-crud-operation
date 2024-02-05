from django.shortcuts import render,redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    user = None
    error_message = None
    if request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        siguser = User.objects.create_user(username=username,email=email,password=password)
        return render(request,'signup.html',{'error':'User Created Successfully'})

    return render(request,'signup.html',{'user':user,'error_message':error_message})
def login_page(request):
    
    msg = None
    # if 'email' in  request.session:
    #     return redirect(home_page)
    
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email,password=password)
        ai = User.objects.all()
        print(email,password)
        print(user)
        if user is not None:
            request.session['email']=email
            return redirect('home_page')
        else:
            return redirect('login')

    

    return render(request,'login.html')

def home_page(request):
    if 'email' in request.session:
        return render(request,'home.html')
    return redirect(login_page)


def admin_page(request):
    
    adminU = User.objects.all()
    

    return render(request,'admin.html',{'adminU':adminU})

def main_page(request):
    return render(request,'main.html')


def createUser(request):
    formPage = True
    adminU = User.objects.all()

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        message = None

        try:
            print('try')
            user = User.objects.create_user(username=username,email=email, password=password)
            message = 'User Created Successfully'
            
            return redirect('admin_page')
        
        except IntegrityError:
            # Handle the case where a user with the given email already exists
            message = 'User with this email already exists'
            return redirect('admin_page')

    return render(request, 'admin.html', {'adminU': adminU, 'formPage': formPage})

def logout_page(request):
    if 'email' in request.session:
        request.session.flush()
    return redirect(login_page)