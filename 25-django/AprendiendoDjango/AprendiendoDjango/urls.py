"""AprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#Pasos para iniciar proyecto en Django
#PASO 1= se ejecuta este codigo, poara iniciar el proyecto django-admin startproject AprendiendoDjango
#PASO 2= Se hacen las migraciones para que se generen archivos y la db, python manage.py migrate
#PASO 3= se corre el servidor, python manage.py runserver
#PASO 4= se crea la app a ensamblar,  python manage.py startapp miapp
#PASO 5= luego, en los views se crea la funcion con las vistas que se desean proyectar
#PASO 6= se importa a las urls y se agrega como nueva URL
from django.contrib import admin
from django.urls import path
from django.conf import settings
#Importar app con mis vistas
from miapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.index, name="index"),
    path('inicio/',  views.index, name="inicio"),
    path('hola_mundo/',  views.hola_mundo, name="hola_mundo"),
    path('pagina-pruebas/', views.pagina, name="Pagina"),
    path('pagina-pruebas/<int:redirigir>', views.pagina, name="Pagina"),
    path('contacto-2/', views.contacto, name="contacto"),
    path('contacto-2/<str:nombre>', views.contacto, name="contacto"),
    path('contacto-2/<str:nombre>/<str:apellido>', views.contacto, name="contacto"),
    path('crear-articulo/<str:title>/<str:content>/<str:public>', views.crear_articulo, name="crear_articulo"),
    path('articulo/', views.articulo, name="articulo"),
    path('editar-articulo/<int:id>', views.editar_Articulo, name="editar_articulo"),
    path('articulos', views.articulos, name="articulos"),
    path('borrar_articulo/<int:id>', views.borrar_articulo, name="borrar_articulo"),
    path('save_articulo/', views.save_articulo, name="save_articulo"),
    path('create_article/', views.create_article, name="create_article"),
    path('create_full_article/', views.create_full_article, name="full_article"),
    
]



#Configuracion para cargar imagenes

if  settings.DEBUG:
    
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    

