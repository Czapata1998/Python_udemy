from flask import Flask, redirect, url_for, render_template
from datetime import datetime

app = Flask(__name__)


# Context procesor 

@app.context_processor

def date_now():
    return {
        'now': datetime.utcnow()
    }

# Endpoints

@app.route('/')
def index():
    
    edad = 101
    
    personas = ['Cristhian', 'Rubio', 'Brayan', 'Kevin']
    
    return render_template('index.html',
                           edad=edad,
                           dato1="Valor1",
                           dato299="Valor2",
                           lista=["uno", "dos", "tres"],
                           personas = personas
                           )

@app.route('/informacion')
@app.route('/informacion/<string:nombre>')
@app.route('/informacion/<string:nombre>/<apellidos>')
def info(nombre=None, apellidos = None):
    texto = ""
    if nombre != None and apellidos != None:
        texto = f" Bienvenido {nombre} {apellidos}"
        
    return render_template ('informacion.html', texto= texto)

@app.route('/contacto')
@app.route('/contacto/<redirecion>')
def contacto(redirecion = None):
    
    if redirecion is not None:
        return redirect(url_for('lenguajes'))
        
    return render_template ('contacto.html')

@app.route('/lenguajes-de-programacion')
def lenguajes():
    return render_template ('lenguajes.html')

if __name__ == '__main__':
    app.run(debug=True)