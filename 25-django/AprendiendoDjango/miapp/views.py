from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article 
from django.db.models import Q
# Create your views here.
#MVC =modelo vista controlador - Acciones metodos
#MVT =modelo vista template - Acciones metodos


layout = """

<h1>Sitio Web con Django / Cristhian Zapata </h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola_mundo">Hola mundo</a>
    </li>
     <li>
        <a href="/pagina-pruebas">Pagina de pruebas</a>
    </li>
    
     <li>
        <a href="/contacto-2">Contacto</a>
    </li>
    
</ul>
<hr/>
"""
 
def index(request):   
    
    # html= """
    #     <h1>Inicio</h1>
    #     <p>Years hasta el 2050: </p>
    #     <ul>
    # """
    # year = 2023
    # while year <= 2050:
    #     if year % 2 ==0:
            
    #         html += f"<li>{str(year)}</li>"
    #     year += 1
        
        
    # html += "</ul>"
    
    year = 2021
    
    hasta = range(year, 2051)
    
    nombre = 'Cristian Zapata'
    
    lenguajes = ['python', 'javascript', 'php', 'java', 'c#']
    
    return render(request,'index.html', {
        'title': 'INICIOOOO',
        'mi_variable': 'Soy un dato que esta en la vista',
        'nombre' : nombre,
        'lenguajes': lenguajes,
        'years': hasta
    }) 
   
    
def hola_mundo(request):
    return render(request, 'hola_mundo.html')
    
   
def pagina(request, redirigir=0):
    
    if redirigir ==1:
        return redirect('contacto', nombre="Cristhian", apellido="Zapata") #Importe el redirect
    
    return render(request, 'pagina.html', {
        'texto': 'brrrr',
        'lista': ['uno', 'dos', 'tres']
    })
    

def contacto(request, nombre="", apellido=""):
    html=""
    
    if nombre and apellido:
        html +=  "<p>El nombre completo es:</p>"
        html += f"<h3> {nombre} {apellido} <h3>"
    
    return HttpResponse(layout+f"<h2>Contacto </h2>"+html)


def crear_articulo(request, title, content, public):
    articulo = Article(
        title= title,
        content = content,
        public = public
    )
    
    articulo.save()
    return HttpResponse(f"Articulo crerado: <strong>{articulo.title}</strong> - {articulo.content}")
    
    
    
    
def articulo(request):
    try:
        articulo = Article.objects.get(id=3, public=True)
        response= f"Articulo: <br/> {articulo.id}. {articulo.title}" 
    except:
        response = "Articulo no encontrado"
        
    return HttpResponse(response)

def editar_Articulo(request, id):
    
    articulo =Article.objects.get(pk=id) 
    
    articulo.title = "Noriel"
    articulo.content = "Jun"
    articulo.public = True
    
    articulo.save()
    
    return HttpResponse(f"Articulo {articulo.id} Editado <strong>{articulo.title}</strong> - {articulo.content}")

def articulos (request):
    articulos = Article.objects.all()
    
    #articulos = Article.objects.filter(id__lte=12, title__contains="2")
    
    articulos =  Article.objects.filter(
        title = "Articulo",
       
        
    ).exclude(
       public = True 
    )
    
    articulos =  Article.objects.filter(
        Q(title__contains="2") | Q(title__contains="4")
    )
    
    #articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='Articulo 2' AND public =0")
    
    return render(request, 'articulos.html', {
        'articulos': articulos
    })
    
    
    
def borrar_articulo(request, id):
    articulo =  Article.objects.get(pk=id)
    articulo.delete()
    
    
    return redirect('articulos')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     
    
    
    
    