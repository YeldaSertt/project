
from django.shortcuts import render
from .forms import RegisterForm,LoginForm

def register(Request):
    form = RegisterForm(data=Request.POST or None)
    return render(Request,'auths/register.html',context={'form':form})
    
def login(request):
    form = LoginForm(request.POST or None)
    return render(request,'auths/login.html',context={"form": form})