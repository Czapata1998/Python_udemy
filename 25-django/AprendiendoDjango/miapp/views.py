from django.shortcuts import render, HttpResponse

# Create your views here.
#MVC =modelo vista controlador - Acciones metodos
#MVT =modelo vista template - Acciones metodos

def hola_mundo(request):
    return HttpResponse("""
                        <h1>Hola mundo con Django</h1>
                        <h3>Mi nombre es Cristhian Zapata</h3>
                    """)
    