# viewdeki urlleri buraya yazıcaz
from django.conf.urls import url

from .views import homepage,bookspecies,favorite,login,register,layout,getMostReadedBooks,allBook,getAdmitBooks
urlpatterns = [
    url(r"^anasayfa/$",homepage,name='homepage'),
    url(r"^bookspecies/$",bookspecies,name='bookspecies'),
    url(r"^favorite/$",favorite,name='favorite'),
    url(r"^login/$",login),
    url(r"^register/$",register),
    url(r"^layout/$",layout),
    url(r"^getMostReadedBooks/$",getMostReadedBooks),
    url(r"^allBook/$",allBook,name="allbook"),
    url(r"^getAdmitBooks/$",getAdmitBooks),
]

