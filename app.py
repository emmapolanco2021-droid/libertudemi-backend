import re
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/registro", methods=["POST"])
def registro():
  datos = request.get_json()

  nombre = datos.get("nombre")
  correo = datos.get("correo")
  password = datos.get("password")

  if not nombre or not correo or not password:
    return (
        jsonify({"exito": False, "mensaje": "Faltan datos obligatorios."}),
        400,
    )

  # Validar seguridad de la contraseña en el backend
  # Al menos 8 caracteres, 1 minúscula, 1 mayúscula, 1 número y 1 carácter especial
  patron_password = (
      r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&._])[A-Za-z\d@$!%*?&._]{8,}$"
  )
  if not re.match(patron_password, password):
    return (
        jsonify({
            "exito": False,
            "mensaje": (
                "La contraseña no cumple con los requisitos de seguridad"
                " (Mínimo 8 caracteres, mayúscula, minúscula, número y carácter"
                " especial)."
            ),
        }),
        400,
    )

  # Aquí puedes guardar el usuario en tu base de datos más adelante
  print(f"Nuevo usuario registrado con éxito: {nombre} ({correo})")

  return jsonify({
      "exito": True,
      "mensaje": (
          f"¡Registro exitoso, {nombre}! Te hemos enviado un correo de"
          " confirmación."
      ),
  })


if __name__ == "__main__":
  app.run(debug=True)
