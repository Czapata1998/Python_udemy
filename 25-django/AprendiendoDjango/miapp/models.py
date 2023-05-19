from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagenes')
    public = models.BooleanField(verbose_name='Publico?')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion') #registra la fecha de creacion
    update_at = models.DateTimeField(auto_now=True, verbose_name='Actualizacion') #Registra la fecha de modificacion
    
    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        verbose_name_plural = 'Articulos'
        ordering = ['create_at']
        
    
class Category(models.Model):
    name= models.CharField(max_length=150)
    description= models.CharField(max_length=500)
    create_at= models.DateField()
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'