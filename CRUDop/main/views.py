from django.shortcuts import render,redirect
from django.db import IntegrityError
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .form import UserForm
from django.views.decorators.cache import never_cache


frm = False
srb = False
message = None
# Create your views here.
@never_cache
def signup(request):
    if 'username' in request.session:
        return render(request,'home.html')
    elif 'isusername' in request.session:
        return render(request,'home.html')
    else:
        if request.method == 'POST':
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            print(username,firstname,lastname,password,email)
            if not (username and email and password and firstname and lastname):
                error_message = "All fields are required."
                return render(request, 'signup.html', {'error_message': error_message})
            
            try:
                siguser = User.objects.create_user(username=username, email=email, password=password,last_name=lastname,first_name=firstname)
                messages.success(request, 'Account created successfully. Please log in.')
                return redirect('login') 
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
                request.session['isusername']=username
                return redirect('admin_page')
            else:
                login(request,user)
                request.session['username']=username
                return redirect('home_page')
        else:
            return redirect('login')

    else:
        if 'username' in  request.session:
            return redirect(home_page)
        elif 'isusername' in request.session:
            return redirect(admin_page)    
        else:
            return render(request,'login.html')

    
@never_cache
def home_page(request):
    if 'username' in request.session:
        return render(request,'home.html')
    elif 'isusername' in request.session:
        return render(request,'home.html')
    else:
        return redirect(login_page)

@never_cache
def admin_page(request):
    frm = False
    if 'isusername' in request.session:

        adminU = User.objects.all
        return render(request,'admin.html',{'adminU':adminU,'frm':frm})
    return  redirect(login_page)
    

def main_page(request):
    return render(request,'main.html')

@never_cache
def createUser(request):
    if 'isusername' in request.session:
    
        formPage = True
        adminU = User.objects.all()

        if request.method == 'POST':
            firstname = request.POST.get('firstname')
            lastname = request.POST.get("lastname")
            email = request.POST.get('email')
            password = request.POST.get('password')
            username = request.POST.get('username')
            message = None

            try:
                print('try')
                user = User.objects.create_user(username=username,email=email, password=password,first_name=firstname,last_name=lastname)
                
                return redirect('admin_page')
            
            except IntegrityError:
                message = 'User with this email or username already exists'
                return render(request, 'admin.html', {'adminU': adminU, 'formPage': formPage, 'error_message': message })

        return render(request, 'admin.html', {'adminU': adminU, 'formPage': formPage})
    
    return  redirect(login_page)


@never_cache
def logout_page(request):
    if 'username' in request.session:
        del request.session['username']
        logout(request)
        return redirect(login_page)
    elif 'isusername' in request.session:
        del request.session['isusername']
        logout(request)
        return redirect(login_page)
    return render(request,'login.html')
    
  
@never_cache
def delete(request,pk):
    if 'isusername' in request.session:
        ins = User.objects.get(pk=pk)
        ins.delete()
        return redirect(admin_page)


    return  redirect(login_page)
    
    
@never_cache
def edit(request, pk):

    if 'isusername' in request.session:
        frm = True
        inst = User.objects.get(id=pk)
        adminU = User.objects.all
        it = 0
        for i in User.objects.values('id'):
            if int(pk) == i['id']:
                it = i['id']
                break
        
        if request.method == 'POST':
            fm = UserForm(request.POST, instance=inst)
            if fm.is_valid():
                fm.save()
                return redirect(admin_page)
        else:
            fm = UserForm(instance=inst)

        return render(request, 'admin.html', {'fm': fm, 'frm': frm, 'inst': inst,'adminU':adminU,'it':it})
    else:
        return redirect(login_page)
    

def search(request):
    srb = True
    if 'isusername' in request.session:
        if request.method == "POST":
            q = request.POST.get('q')
            adminU = User.objects.filter(Q(username__istartswith=q)).order_by('-date_joined')
            if len(adminU):
                return render(request, 'admin.html',{'srb':srb ,'adminU':adminU})
            else:
                message = 'There is no user found'
                return render(request,'admin.html',{'srb':srb ,'adminU':adminU,'message':message})
            #if user is not found then show message to the user that no users are available with this name  


        return redirect(admin_page)
    else:
        return redirect(login_page)