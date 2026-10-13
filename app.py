from flask import Flask, jsonify, request
from flask_cors import CORS  # Permite que la página web se comunique con el servidor

app = Flask(__name__)
CORS(app)  # Habilitamos CORS para evitar bloqueos del navegador

# Ruta de prueba para verificar que el servidor de Libertademi está activo
@app.route("/")
def inicio():
    return "¡El backend de Libertademi está funcionando correctamente! 🚀"

# Ruta para recibir el registro de nuevos usuarios (Futura Base de Datos)
@app.route("/api/registro", methods=["POST"])
def registrar_usuario():
    datos = request.get_json()
    
    nombre = datos.get("nombre")
    correo = datos.get("correo")
    password = datos.get("password")
    
    # Aquí más adelante conectaremos la base de datos SQLite para guardarlos de forma segura
    print(f"📥 Nuevo usuario recibido -> Nombre: {nombre}, Correo: {correo}")
    
    # Respondemos con éxito al Frontend (script.js)
    return jsonify({
        "exito": True,
        "mensaje": f"¡Bienvenido a Libertademi, {nombre}! Tu registro se ha completado."
    })

if __name__ == "__main__":
    # Arrancamos el servidor en el puerto 5000
    app.run(debug=True, port=5000)