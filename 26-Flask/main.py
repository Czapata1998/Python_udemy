from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "Aprendiendo flask"

@app.route('/informacion')
@app.route('/informacion/<string:nombre>')
@app.route('/informacion/<string:nombre>/<apellidos>')
def info(nombre=None, apellidos = None):
    texto = ""
    if nombre != None and apellidos != None:
        texto = f"<h3> Bienvenido {nombre} {apellidos}</h3>"
    return f"""
                <h1> Pagina de informacion </h1>
                <p>Esta es la paginacion </p>
                {texto}
    """

@app.route('/contacto')
@app.route('/contacto/<redirecion>')
def contacto(redirecion = None):
    
    if redirecion is not None:
        return redirect(url_for('lenguajes'))
        
    return "<h1> Pagina de contacto </h1>"

@app.route('/lenguajes-de-programacion')
def lenguajes():
    return "<h1> Pagina de lenguajes </h1>"

if __name__ == '__main__':
    app.run(debug=True)