from flask import Flask, request, render_template
import os
import random
import platform
from clases.accion import Accion 
from clases.comedia import Comedia 
from clases.drama import Drama

app = Flask(__name__,template_folder='html')

@app.route("/")
def películas():
    return render_template("start_películas.html")

@app.route("/películas", methods=['POST'])
def mostrar_películas():
 # Obtener la película seleccionada por el usuario
    nombre = request.form['película']

 # Insertar el código aquí
    if nombre == "Acción":
        anyo = request.form['anyo']
        protagonista = request.form['protagonista']
        pelicula_ingresada = Accion(nombre, anyo, protagonista)
    elif nombre == "Comédia":
        anyo = request.form['anyo']
        director = request.form['director']
        pelicula_ingresada = Comedia(nombre, anyo, director)
    elif nombre == "Drama":
        anyo = request.form['anyo']
        tema = request.form['tema']
        pelicula_ingresada = Drama(nombre, anyo, tema)

 # Renderizar la página de películas con la película seleccionada
    return render_template("películas.html", película=pelicula_ingresada)


if __name__ == '__main__':
   app.run(debug=True)