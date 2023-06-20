from django.db import models

# Create your models here.

class Category(models.model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='descripcion')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el: ')
    
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    def __str__(self):
        return self.name