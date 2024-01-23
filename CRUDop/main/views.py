from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    user = None
    error_message = None
    if request.POST:
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        print(userid,password)
        try:
             user = User.objects.create_user(username=userid,password=password)
        except Exception as e:
            error_message=str(e)

    return render(request,'signup.html',{'user':user,'error_message':error_message})
def login_page(request):
    return render(request,'login.html')

def home_page(request):
    return render(request,'home.html')

def admin_page(request):
    return render(request,'admin.html')

def main_page(request):
    return render(request,'main.html')