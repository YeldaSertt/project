# viewdeki urlleri buraya yazıcaz
from django.conf.urls import url

from .views import home_page,Merhaba_Django,product,novel
urlpatterns = [
    url(r"^Merhaba/$",Merhaba_Django),
    url(r"^Homepage/$",home_page),
    url(r"^Product/$",product),
    url(r"^Product/Novel/$",novel),
]

