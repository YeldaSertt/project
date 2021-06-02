from django.conf.urls import url
from .views import register,user_login,user_logout,user_profile

urlpatterns = [
    url(r"^register/$",register,name='register'),
    url(r"^login/$",user_login,name='user_login'),
    url(r"^logout/$",user_logout,name='user_logout'),
    url(r"^(?P<username>[-\w]+)/$",view=user_profile,name='user-profile')
]