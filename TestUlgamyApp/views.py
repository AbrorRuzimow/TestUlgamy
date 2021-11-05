from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def Login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if request.user.user_type == '1':
                return HttpResponseRedirect(reverse('AdminDashboard'))
            elif request.user.user_type == '2':
                return HttpResponseRedirect(reverse('MugallymDashboard'))
            elif request.user.user_type == '3':
                return HttpResponseRedirect(reverse('StudentDashboard'))
        else:
            messages.info(request,'Ulanyjynyň adyny ya-da açar sözüni ýalňyş girizdiňiz')
            messages.warning(request,'btn-danger')
            messages.error(request,'card-danger')
            return HttpResponseRedirect(reverse('Login'))
    return render(request,'Login.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login'))