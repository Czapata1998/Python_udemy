from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(default='null')
    public = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True) #registra la fecha de creacion
    update_at = models.DateTimeField(auto_now=True) #Registra la fecha de modificacion
    
    
    
class Category(models.Model):
    name= models.CharField(max_length=150)
    description= models.CharField(max_length=500)
    create_at= models.DateField()