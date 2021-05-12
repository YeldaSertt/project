from django.db import models


# Create your models here.
class book_species(models.Model):
    id = models.BigAutoField(primary_key=True)
    species_name = models.CharField( max_length=30,blank=True)

class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    author_name = models.CharField(max_length=30,blank=False,verbose_name="Yazar Adı") 
    author_lastname = models.CharField(max_length=30,blank=False,verbose_name="Yazarın Soyadı") 

class book(models.Model):
    id = models.BigAutoField(primary_key=True)     
    name = models.CharField(max_length=30,blank=False,verbose_name="Kitap Adı")
    sayfa_sayisi = models.IntegerField(blank=True)
    yayin_tarihi = models.DateTimeField(blank=True)
    book_species_id = models.ForeignKey(book_species,on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author,on_delete=models.CASCADE)
    # book = models.OneToOneField(book_species,on_delete=models.CASCADE,primary_key=True)  
    

    
    