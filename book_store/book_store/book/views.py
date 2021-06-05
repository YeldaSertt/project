
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.urls.base import reverse_lazy
from book.models import book,book_species,author
import json
from django.core import serializers
from datetime import datetime
from django.contrib.auth import authenticate
import dateparser
from django.contrib.auth.decorators import login_required
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
        yayin_tarihi = None
        if o["yayin_tarihi"]:
            # yayin_tarihi = dateparser.parse(str(o["yayin_tarihi"]), date_formats=["%Y-%d-%m"]).strftime("%Y-%m-%d")
            yayin_tarihi = datetime.strptime(o["yayin_tarihi"],'%d.%m.%Y').strftime('%Y-%m-%d')
        book1 = book(book_name = o["book_name"],
                            sayfa_sayisi = o["sayfa_sayisi"] if o["sayfa_sayisi"] else 0,
                            yayin_tarihi= yayin_tarihi,
                            species_id=species,
                            author_id = author1,
                            image =o["images"][0] if o["images"] else "",
                            star = str(o["star"]),
                            desc = o["desc"]
                            )

        book1.save()
  
# Create your views here.
def homepage(Request):
    # fileRead()
    book_list = book.objects.all()
    return render(Request,'homepage.html',context = {"book_list":book_list})

def bookspecies(Request):
    book_list = book.objects.all()
    species_list = book_species.objects.all()
    return render(Request,'book_species/bookspecies.html',context = {"book_list":book_list,"species_list":species_list})

def getBookSpecies(Request, species_id): 
    book_species_list  = book.objects.filter(species_id__species_id=species_id)
    species_list = book_species.objects.all()
    return render(Request,'book_species/bookspecies.html',context = {"book_list":book_species_list,"species_list":species_list})
 
# @login_required(login_url="/bookstore/login/")
# @login_required(login_url=reverse_lazy("user_login"))
@login_required  #settingsde login url eklendi
def blog(request):
    # # kullanıcı login kontrolü.
    # if not request.user.is_authenticated: 
    #     return HttpResponseRedirect(reverse("user_login"))
    book_list = book.objects.all()
    # return render(request,'blog/blog.html',context = {"book_list":book_list})
    return render(request,'blog/blog_homepage.html',context = {"book_list":book_list})
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

def getBookDetails(Request,book_id):
    book_detail_list  = book.objects.filter(book_id=book_id)
    return render(Request,'details/getdetails.html',context={"book_detail_list":book_detail_list})
    


def login():
    pass
def register():
    pass
def layout():
    pass

