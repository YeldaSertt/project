
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from book.models import book,book_species,author
import json
from django.core import serializers
from datetime import date
import dateparser

def fileRead():
    with open('book/book2.json', 'r') as f:
        data=f.read()
    obj = json.loads(data)

    # obj = json.loads(file)
    
    databaseInsert(obj)
#         record = Country(name = o)
#         record.save()
def databaseInsert(obj):
    for o in obj:
        species = book_species(species_name= o["tur"])
        species.save()
        author1 = author(author_name=o["author"])
        author1.save()
        book1 = book(book_name = o["book_name"],
                            sayfa_sayisi = o["sayfa_sayisi"] if o["sayfa_sayisi"] else 0,
                            yayin_tarihi= "2021-05-05",
                            species_id=species,
                            author_id = author1,
                            image =o["images"][0] if o["images"] else "",
                            star = str(o["star"]),
                            desc = o["desc"]
                            )

        book1.save()

        # print(o)
# def Db_save():

#     species1 = book_species(species_name="Fantastik")
#     species1.save()
#     species2 = book_species(species_name="Roman")
#     species2.save()
#     species3 = book_species(species_name="Macara")
#     species3.save()
   
#     book_author1 = Author(author_name="J.L",author_lastname="Rowling")
#     book_author1.save()
#     book_author2 = Author(author_name="Jules",author_lastname="Verne")
#     book_author2.save()
   
#     book_author = book(name = "Harry Potther",sayfa_sayisi=500,yayin_tarihi=date(2005, 7, 27),book_species_id=species1,author_id=book_author1)
#     book_author.save()
#     book_author = book(name = "80 Günde Devri Alem",sayfa_sayisi=100,yayin_tarihi=date(2005, 7, 27),book_species_id=species3,author_id=book_author2)
#     book_author.save()
#     book_author = book(name = "Denizler Altında ",sayfa_sayisi=200,yayin_tarihi=date(2005, 7, 27),book_species_id=species2,author_id=book_author2)
#     book_author.save()

    
# Create your views here.
def homepage(Request):
    # fileRead()
    book_list = book.objects.all()
    # Db_save()
    return render(Request,'homepage.html',context = {"book_list":book_list})

def bookspecies(Request):
    book_list = book.objects.all()
    return render(Request,'bookspecies.html',context = {"book_list":book_list})
def blog():
    pass

def favorite(Request):
    book_list = book.objects.all()
    return render(Request,'favorite/favorite.html',context={"book_list":book_list})
    
def getMostReadedBooks(Request): 
    book_list = book.objects.filter(author_id=1)
    book_list1 = list(book_list.values())
    return JsonResponse(book_list1,safe=False)

def allBook(Request):
    
    book_list = book.objects.all()
    return render(Request,'favorite/favorite.html',context={"book_list":book_list})

def getAdmitBooks(Request): 
    book_list = book.objects.filter(author_id=2)
    book_admit = list(book_list.values())
    return JsonResponse(book_admit,safe=False)

def login():
    pass
def register():
    pass
def layout():
    pass

