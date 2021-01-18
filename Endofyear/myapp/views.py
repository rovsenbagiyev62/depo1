from django.shortcuts import render
from myapp.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import logout,login,authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request,'myapp/index.html')
def bonus(request):
    return render(request,'myapp/bonus.html')
def lichess(request):
    return render(request,'myapp/lichess.html')
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            x = user_form.save()
            x.set_password(x.password)
            x.save()
            profile = profile_form.save(commit=False)
            profile.ido = x
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'myapp/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if  request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        us = authenticate(username = username,password=password)
        if us:
            if us.is_active:
                login(request,us)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account is not Active ')
        else:
            print('Someone tried and failed')
            print('Username: {} and Password:{}'.format(username,password))
            return HttpResponse('INVALID DETAILS')
    else:
        return render(request,'myapp/login.html',{})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('bonus'))
@login_required
def special(request):
    return HttpResponse('Welcome')

def tolgaçalım(request):
    return render(request,'myapp/tolga.html')