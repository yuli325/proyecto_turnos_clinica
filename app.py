from flask import Flask

app = Flask(__name__)

# Ruta principal
@app.route('/')
def inicio():
    return "Bienvenido al Sistema de Turnos – Clínica XYZ"

# Ruta dinámica para citas
@app.route('/cita/<paciente>')
def cita(paciente):
    return f"Hola {paciente}, tu cita médica está en proceso."

# Otra ruta dinámica de ejemplo
@app.route('/turno/<nombre>')
def turno(nombre):
    return f"Turno de {nombre} confirmado. ¡Gracias por usar nuestro sistema!"

if __name__ == '__main__':
    app.run(debug=True)