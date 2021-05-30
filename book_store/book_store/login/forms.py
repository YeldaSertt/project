
from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from django.contrib.auth import authenticate

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name','last_name','username','email','password']
        
    def __init__(self,*args,**kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class':'form-control'}


class LoginForm(forms.Form):
    username = forms.CharField(required=True,max_length=50,label="Username",widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(required=True,max_length=50,label="Password", widget=forms.PasswordInput(attrs={"class":"form-control"}))

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username= username, password = password)
        if not user:
            raise forms.ValidationError("Hatalı kullanıcı adı veya şifre girdiniz.")

