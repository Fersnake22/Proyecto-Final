
from flask import Flask, render_template, request, redirect, flash
import controlador_citas
from Base_De_Datos import create_tables

app = Flask(__name__)

"""
Definición de rutas
"""


@app.route("/agregar_cita")
def formulario_agregar_cita():
    return render_template("agregar_cita.html")


@app.route("/guardar_cita", methods=["POST"])
def guardar_cita():
    nombre = request.form["nombre"]
    consulta = request.form["consulta"]
    telefono = request.form["telefono"]
    controlador_citas.insertar_cita(nombre, consulta, telefono)
    return redirect("/citas")


@app.route("/")
@app.route("/citas")
def citas():
    citas = controlador_citas.obtener_citas()
    return render_template("citas.html", citas=citas)


@app.route("/eliminar_cita", methods=["POST"])
def eliminar_cita():
    controlador_citas.eliminar_cita(request.form["id"])
    return redirect("/citas")


@app.route("/formulario_editar_cita/<int:id>")
def editar_cita(id):
    # Obtener el cita por ID
    cita = controlador_citas.obtener_cita_por_id(id)
    return render_template("editar_cita.html", cita=cita)


@app.route("/actualizar_cita", methods=["POST"])
def actualizar_cita():
    id = request.form["id"]
    nombre = request.form["nombre"]
    consulta = request.form["consulta"]
    telefono = request.form["telefono"]
    controlador_citas.actualizar_cita(nombre, consulta, telefono, id)
    return redirect("/citas")


# Iniciar el servidor
if __name__ == "__main__":
    create_tables()
 
    app.run(port=8028, debug=True)
from api import principal