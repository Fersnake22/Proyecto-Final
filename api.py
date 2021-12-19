
from flask import Flask, render_template, request, redirect, flash, jsonify
import controlador_citas
from Base_De_Datos import create_tables

app = Flask(__name__)

"""
Definición de rutas
"""

@app.route("/citas")
def citas():
    citas = controlador_citas.obtener_citas()
    return jsonify(citas)


@app.route("/cita", methods=["GET"])
def guardar_cita():
    cita_detalles = request.get_json()
    nombre = cita_detalles["nombre"]
    consulta = cita_detalles["consulta"]
    telefono = cita_detalles["telefono"]
    resultado = controlador_citas.insertar_cita(nombre, consulta, telefono)
    return redirect("/citas")
    return jsonify(resultado)




@app.route("/cita", methods=["DELETE"])
def eliminar_cita():
    resultado = controlador_citas.eliminar_cita(cita_detalles["id"])
    return jsonify(resultado)


@app.route("/cita/<int:id>")
def editar_cita(id):
    # Obtener el cita por ID
    cita = controlador_citas.obtener_cita_por_id(id)
    return jsonify(cita)


@app.route("/cita", methods=["PUT"])
def actualizar_cita():
    cita_detalles = request.get_json()
    id = cita_detalles["id"]
    nombre = cita_detalles["nombre"]
    consulta = cita_detalles["consulta"]
    telefono = cita_detalles["telefono"]
    resultado = controlador_citas.actualizar_cita(nombre, consulta, telefono, id)
    return jsonify(resultado)

@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:8010/"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "GET, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


def principal():
   
    create_tables()

    app.run(port=8027, debug=False)

principal()