
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from book.models import book,book_species,author
import json
from django.core import serializers
from datetime import datetime


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
        species = o["tur"]
        species_list = book_species.objects.filter(species_name=o["tur"])
        if species_list:
            species = species_list[0]
        else:
            species = book_species(species_name= o["tur"])
            species.save()   
                  
        
        author1 = author(author_name=o["author"])
        author1.save()

        book1 = book(book_name = o["book_name"],
                            sayfa_sayisi = o["sayfa_sayisi"] if o["sayfa_sayisi"] else 0,
                            yayin_tarihi= "2008-02-06",
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
    return render(Request,'homepage.html',context = {"book_list":book_list})

def bookspecies(Request):
    species_list  = book.objects.filter(species_id__species_name='fantastik')
    return render(Request,'book_species/bookspecies.html',context= {"book_list":species_list})

def bookspeciesani(Request):
    species_list  = book.objects.filter(species_id__species_name='manga')
    return render(Request,'book_species/bookspecies.html',context= {"book_list":species_list})
# def getBookSpecies(Request): 
#     species_list  = book.objects.filter(species_id__species_name='manga')
#     book_list1 = list(book_list.values())
#     return JsonResponse(book_list1,safe=False)
# def getBookSpecies(request, id):
#     print(id)
#     species_list  = book.objects.filter(species_id__species_name='manga')
#     context = {'book_list':species_list,'request':request}
#     mytemplate  = loader.get_template('book_species/bookspecies.html')
#     html = mytemplate.render(context)
#     return HttpResponse(html)

def blog():
    pass

def favorite(Request):
    book_list = book.objects.all()
    return render(Request,'favorite/favorite.html',context={"book_list":book_list})
    
def getMostReadedBooks(Request): 
    book_list = book.objects.filter(star="5")
    book_list1 = list(book_list.values())
    return JsonResponse(book_list1,safe=False)

def allBook(Request):
    
    book_list = book.objects.all()
    return render(Request,'favorite/favorite.html',context={"book_list":book_list})

def getAdmitBooks(Request): 
    book_list = book.objects.filter(star="5",start="4")
    book_admit = list(book_list.values())
    return JsonResponse(book_admit,safe=False)

def login():
    pass
def register():
    pass
def layout():
    pass

