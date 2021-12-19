
from Base_De_Datos import obtener_db


def insertar_cita(nombre, telefono, consulta):
    db = obtener_db()
    cursor = db.cursor()
    sentencia = "INSERT INTO citas(nombre, telefono, consulta) VALUES (?, ?, ?)"
    cursor.execute(sentencia, [nombre, telefono, consulta])
    db.commit()
    return True

def obtener_citas():
    db = obtener_db()
    cursor = db.cursor()
    query = "SELECT id, nombre, telefono, consulta FROM citas"
    cursor.execute(query)
    return cursor.fetchall()

def eliminar_cita(id):
    db = obtener_db()
    cursor = db.cursor()
    sentencia = "DELETE FROM citas WHERE id = ?"
    cursor.execute(sentencia, [id])
    db.commit()
    return True

def obtener_cita_por_id(id):
    db = obtener_db()
    cursor = db.cursor()
    sentencia = "SELECT id, nombre, telefono, consulta FROM citas WHERE id = ?"
    cursor.execute(sentencia, [id])
    return cursor.fetchone()

def actualizar_cita(id, nombre, telefono, consulta):
    db = obtener_db()
    cursor = db.cursor()
    sentencia = "UPDATE citas SET nombre = ?, telefono = ?, consulta = ? WHERE id = ?"
    cursor.execute(sentencia, [nombre, telefono, consulta, id])
    db.commit()
    return True
