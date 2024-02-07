from django.shortcuts import render,redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .form import UserForm
from django.views.decorators.cache import never_cache




# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not (username and email and password):
            error_message = "All fields are required."
            return render(request, 'signup.html', {'error_message': error_message})
        
        try:
            siguser = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')  # Assuming you have a login URL named 'login'
        except Exception as e:
            error_message = 'Usser already exist'
            return render(request, 'signup.html', {'error_message': error_message})

    return render(request, 'signup.html')
@never_cache
def login_page(request):
    
    msg = None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        ai = User.objects.all()
        print(username,password)
        print(user)
        if user is not None:
            if user.is_superuser:
                login(request,user)
                request.session['username']=username
                return redirect('admin_page')
            login(request,user)
            request.session['username']=username
            return redirect('home_page')
        else:
            return redirect('login')

    else:
        if 'username' in  request.session:
            return redirect(home_page)
        else:
            return render(request,'login.html')

    
@never_cache
def home_page(request):
    if 'username' in request.session:
        return render(request,'home.html')
    else:
        return redirect(login_page)

def admin_page(request):
    if 'username' in request.session:

        adminU = User.objects.all
        return render(request,'admin.html',{'adminU':adminU})
    return  redirect(login_page)
    

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
            message = 'User with this email already exists'
            return redirect('admin_page')

    return render(request, 'admin.html', {'adminU': adminU, 'formPage': formPage})


@never_cache
def logout_page(request):
    if 'username' in request.session:
        del request.session['username']
        logout(request)
        return redirect(login_page)
    
  

def delete(request,pk):
    ins = User.objects.get(pk=pk)
    ins.delete()
    return redirect(admin_page)

def edit(request, pk):
    frm = True
    inst = User.objects.get(id=pk)
    
    if request.method == 'POST':
        fm = UserForm(request.POST, instance=inst)
        if fm.is_valid():
            fm.save()
            return redirect(admin_page)
    else:
        fm = UserForm(instance=inst)

    return render(request, 'admin.html', {'fm': fm, 'frm': frm, 'inst': inst})