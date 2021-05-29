
from django import forms
from django.contrib.auth.models import User
from django.forms import fields

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name','last_name','username','email','password']



    def __init__(self,*args,**kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class':'form-control'}