from django.db import models

# Create your models here.
class book_species(models.Model):
    species_id = models.BigAutoField(primary_key=True)
    species_name = models.CharField( max_length=30,blank=True)

class author(models.Model):
    author_id = models.BigAutoField(primary_key=True)
    author_name = models.CharField(max_length=30,blank=False,verbose_name="Yazar Adı") 
    author_lastname = models.CharField(max_length=30,blank=False,verbose_name="Yazarın Soyadı") 

class book(models.Model):
    book_id = models.BigAutoField(primary_key=True)     
    book_name = models.CharField(max_length=30,blank=False,verbose_name="Kitap Adı")
    sayfa_sayisi = models.IntegerField(blank=True)
    yayin_tarihi = models.DateTimeField(blank=True)
    species_id = models.ForeignKey(book_species,on_delete=models.CASCADE)
    author_id = models.ForeignKey(author,on_delete=models.CASCADE)
    image = models.CharField(max_length=200,blank=False)
    star = models.CharField(max_length=200,blank=False)
    desc = models.CharField(max_length=500,blank=False)

class comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True) 
    book_id =models.ForeignKey(book,on_delete=models.CASCADE)      
    description = models.CharField(max_length=100,blank=False,verbose_name="Kitap Adı")
    comment_admit = models.IntegerField(blank=True)

class authority(models.Model):
    yetki_id = models.BigAutoField(primary_key=True)
    admin = models.CharField(max_length=100,blank=False)
    users = models.CharField(max_length=100,blank=False)

class persons(models.Model):
    person_id = models.BigAutoField(primary_key=True)
    person_name = models.CharField(max_length=100,blank=False)
    person_surname = models.CharField(max_length=100,blank=False)
    nick_name = models.CharField(max_length=100,blank=False)
    description = models.CharField(max_length=100,blank=False)
    description = models.CharField(max_length=100,blank=False)
    photo = models.CharField(max_length=200,blank=False)
    pasword = models.CharField(max_length=200,blank=False)
    comment_id = models.ForeignKey(comment,on_delete=models.CASCADE)
    yetki_id = models.ForeignKey(authority,on_delete=models.CASCADE)


    
    



    # book = models.OneToOneField(book_species,on_delete=models.CASCADE,primary_key=True)  
    

    
    