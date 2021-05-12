
from django.shortcuts import render,HttpResponse
from book.models import book,book_species,Author
from datetime import date


def Db_save():

    species1 = book_species(species_name="Fantastik")
    species1.save()
    species2 = book_species(species_name="Roman")
    species2.save()
    species3 = book_species(species_name="Macara")
    species3.save()
   
    book_author1 = Author(author_name="J.L",author_lastname="Rowling")
    book_author1.save()
    book_author2 = Author(author_name="Jules",author_lastname="Verne")
    book_author2.save()
   
    book_author = book(name = "Harry Potther",sayfa_sayisi=500,yayin_tarihi=date(2005, 7, 27),book_species_id=species1,author_id=book_author1)
    book_author.save()
    book_author = book(name = "80 Günde Devri Alem",sayfa_sayisi=100,yayin_tarihi=date(2005, 7, 27),book_species_id=species3,author_id=book_author2)
    book_author.save()
    book_author = book(name = "Denizler Altında ",sayfa_sayisi=200,yayin_tarihi=date(2005, 7, 27),book_species_id=species2,author_id=book_author2)
    book_author.save()

    
# Create your views here.
def Merhaba_Django(Request):

    book_list = book.objects.all()
    # for q in query:
    #     print(q.name)
    # Db_save()
    return render(Request,'homepage.html',context = {"book_list":book_list})

def home_page():
    return render(Request,'homepage.html')
def product():
    pass

def drama():
    pass
def novel():
    pass
