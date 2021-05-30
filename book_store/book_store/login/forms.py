
from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from django.contrib.auth import authenticate

class RegisterForm(forms.ModelForm):
    password = forms.CharField(min_length=5,required=True,label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_confirm = forms.CharField(min_length=5,required=True,label='Password Control',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields=['first_name','last_name','username','email','password','password_confirm']
        
    def __init__(self,*args,**kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class':'form-control'}
        self.fields['first_name'].required=True
        self.fields['last_name'].required=True

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            self.add_error('password','Parolalar Eşleşmiyor')
            self.add_error('password_confirm','Parolalar Eşleşmiyor')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email =email.lower()
        print( email)
        if  User.objects.filter(email=email).exists():         
            raise forms.ValidationError('Bu email sistemde kayıtlı')
        return email


class LoginForm(forms.Form):
    username = forms.CharField(required=True,max_length=50,label="Kullanıcı Adı",widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(required=True,max_length=50,label="Şifre", widget=forms.PasswordInput(attrs={"class":"form-control"}))

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username= username, password = password)
        if not user:
            raise forms.ValidationError("Hatalı kullanıcı adı veya şifre girdiniz.")

