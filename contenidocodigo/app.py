from flask import Flask, request, render_template

app = Flask(__name__,template_folder='html')

@app.route("/")
def películas():
    return render_template("start_películas.html")

@app.route("/películas", methods=['POST'])
def mostrar_películas():
 # Obtener la película seleccionada por el usuario

 # Insertar el código aquí
        
 # Renderizar la página de películas con la película seleccionada
 return render_template("películas.html", película=película_ingresada)


if __name__ == '__main__':
   app.run(debug=True)