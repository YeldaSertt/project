# viewdeki urlleri buraya yazıcaz
from django.conf.urls import url

from .views import homepage,bookspecies,favorite,login,register,layout,getMostReadedBooks,allBook,getAdmitBooks,getBookSpecies,getBookDetails
urlpatterns = [
    url(r"^anasayfa/$",homepage,name='homepage'),
    url(r"^kategoriler/$",bookspecies,name='bookspecies'),
    url(r"^favorite/$",favorite,name='favorite'),
    # url(r"^login/$",login),
    # url(r"^register/$",register),
    url(r"^layout/$",layout),
    url(r"^getMostReadedBooks/$",getMostReadedBooks),
    url(r"^allBook/$",allBook,name="allbook"),
    url(r"^getAdmitBooks/$",getAdmitBooks),
    url(r"^kitap_turleri/(?P<species_id>[0-9]+)/$",getBookSpecies,name="getBookSpecies"),
    url(r"^book/details/(?P<book_id>[0-9]+)/$",getBookDetails,name="getBookDetails"),
]

