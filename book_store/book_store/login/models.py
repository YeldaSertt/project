from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

class UserProfile(models.Model):
    SEX = ((None,'Lütfen cinsiyet giriniz!!'),('diger','DİGER'),('erkek','ERKEK'),('kadın','KADIN'))
    user =models.OneToOneField(User,null=True,verbose_name='User',on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000,verbose_name="Hakkımda",blank=True,null=True)
    profile_photo = models.ImageField(null=True,blank=True,verbose_name='Profile Fotografı')
    dogum_tarihi = models.DateField(null=True,blank=True,verbose_name='Dogum Tarihi')
    sex = models.CharField(choices=SEX,blank=False,null=True,max_length=10,verbose_name='Cinsiyet')
    
    class Meta:
        verbose_name_plural ='Kullanici Profilleri'

    def get_screen_name(self):
        user = self.user
        if user.get_full_name():
            return user.get_full_name
        return user.username

    def user_profile_url(self):
        url = reverse('user-profile',kwargs={'username':self.user.username})
        return url
    def user_url(userName):
            print("aaaaaaaaaaaaa",userName)
            url='user_profile'
            return url

    def get_profile_image(self):
        if self.profile_photo:
            return self.profile_photo.url
        return "/static/images/demo/defaultfoto.png"

def __str__(self):
    return '%s Profile'% (self.get_screen_name())