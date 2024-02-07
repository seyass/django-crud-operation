"""
URL configuration for CRUDop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_page,name='login'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_page,name='login'),
    path('home/',views.home_page,name='home_page'),
    path('admin1/',views.admin_page,name='admin_page'),
    path('createUser/',views.createUser,name='createUser'),
    path('logout/',views.logout_page,name='logout_page'),
    path('delete/<pk>',views.delete,name='delete'),
    path('edit/<pk>',views.edit,name='edit')
    
]