from django.shortcuts import render, HttpResponse

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
    
</ul>
<hr/>
"""
 
def index(request):   
    
    html= """
        <h1>Inicio</h1>
        <p>Years hasta el 2050: </p>
        <ul>
    """
    year = 2023
    while year <= 2050:
        if year % 2 ==0:
            
            html += f"<li>{str(year)}</li>"
        year += 1
        
        
    html += "</ul>"
    
    return HttpResponse(layout+html) 
   
    
def hola_mundo(request):
    return HttpResponse(layout+"""
                        <h1>Hola mundo con Django</h1>
                        <h3>Mi nombre es Cristhian Zapata</h3>
                    """)
    
   
def pagina(request):
    return HttpResponse(layout+"""
        <h1>Pagina de mi web </h1>   
        <p>Creado por Cristhian Zapata</p>            
""")
    

def contacto(request, nombre="", apellido=""):
    html=""
    
    if nombre and apellido:
        html +=  "<p>El nombre completo es:</p>"
        html += f"<h3> {nombre} {apellido} <h3>"
    
    return HttpResponse(layout+f"<h2>Contacto </h2>"+html)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     
    
    
    
    