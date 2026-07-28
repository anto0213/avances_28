from flask import Flask, render_template, request, redirect

# Importamos la clase de mascota.py
from mascota import Mascota
app = Flask(__name__)
@app.route("/")
def index():

   # Invocamos al método de clase get all para obtener todas las mascotas
   mascotas = Mascota.get_all()
   print(mascotas)

   #Crea un archivo index.html para que se por lo pronto
   return render_template("index.html", mascotas = mascotas)

@app.route("/agregar_mascota", methods=["POST"])
def agregar_mascota():
      data = {
         "nombre": request.form["nombre"],
         "tipo": request.form["tipo"],
         "color": request.form["color"]
      }
      # Invocamos al método de clase save para guardar la mascota
      Mascota.save(data)
      return redirect("/")
if __name__ == "__main__":
       app.run(debug=True)