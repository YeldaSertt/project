
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import get_messages
from .forms import RegisterForm,LoginForm



def register(request):
    # if request.user.is_authenticated: 
    #     return HttpResponseRedirect(reverse("homepage"))
    if not request.user.is_anonymous: 
        return HttpResponseRedirect(reverse("homepage"))
    form = RegisterForm(data=request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        username = form.cleaned_data.get("username")
        user.set_password(password)
        user.save()
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                messages.success(request,'<b> Tebrikler başarılı </b>',extra_tags='success')
                return HttpResponseRedirect(reverse('homepage'))
    return render(request,'auths/register.html',context={'form':form})
    
def user_login(request):
    if not request.user.is_anonymous: 
        return HttpResponseRedirect(reverse("homepage"))
    form = LoginForm(request.POST or None)
    if form.is_valid():      
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                msg = "Hoşgeldin"
                messages.success(request,msg,extra_tags='success')
                return HttpResponseRedirect(reverse('homepage'))
    return render(request,'auths/login.html',context={"form": form})

def user_logout(request):
    username = request.user.username  # o an hangi user giriş yaptıysa kullanıcı alabiliyoruz.
    logout(request)
    msg = "<b> SİSTEMDEN ÇIKIŞ YAPTINIZ %s </b>"%(username)
    print("--------------",msg)
    messages.success(request,msg,extra_tags='success')
    return HttpResponseRedirect(reverse('user_login'))

def user_profile(request,username):
    user =  get_object_or_404(User,username=username)
    return render(request,'',context={"user":user})