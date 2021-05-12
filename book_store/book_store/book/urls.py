# viewdeki urlleri buraya yazıcaz
from django.conf.urls import url

from .views import homepage,bookspecies,favorite,login,register,layout
urlpatterns = [
    url(r"^anasayfa/$",homepage),
    url(r"^bookspecies/$",bookspecies),
    url(r"^favorite/$",favorite),
    url(r"^login/$",login),
    url(r"^register/$",register),
    url(r"^layout/$",layout),
]

