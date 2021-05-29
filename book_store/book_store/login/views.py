
from django.shortcuts import render
from .forms import RegisterForm

def register(Request):
    form = RegisterForm(data=Request.POST or None)
    return render(Request,'auth/register.html',context={'form':form})