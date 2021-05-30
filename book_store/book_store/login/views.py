
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import RegisterForm,LoginForm

def register(Request):
    form = RegisterForm(data=Request.POST or None)
    print("++++",form)
    if form.is_valid():
        print("----")
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        username = form.cleaned_data.get("username")
        user.set_password(password)
        user.save()
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(Request)
                messages.success(Request,'<b> Tebrikler başarılı </b>',extra_tags='success')
                return HttpResponseRedirect(reverse('homepage'))
    return render(Request,'auths/register.html',context={'form':form})
    
def login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                msg = "Hoşgeldin"%(username)
                messages.success(request,msg,extra_tags='success')
                return HttpResponseRedirect(reverse('homepage'))
    return render(request,'auths/login.html',context={"form": form})