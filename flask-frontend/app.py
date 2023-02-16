import werkzeug
from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)
app.debug = True  # Activar el modo de depuración
app.secret_key = ""

headers = {
    'Authorization': 'Bearer TOKEN JWT'
}
url = "http://127.0.0.1:8000/api/estudiantes/"


@app.route("/")
def hello():
    return render_template('home.html')


@app.route("/inscribir", methods=['POST', 'GET'])
def inscribir():
    """Inscribe un estudiantes realizando un POST a la base de datos"""
    if request.method == 'POST':
        # datos del formulario
        primerNombre = request.form['primer_nombre']
        segundo_nombre = request.form['segundo_nombre']
        primer_apellido = request.form['primer_apellido']
        segundo_apellido = request.form['segundo_apellido']
        fecha_nacimiento = request.form['fecha_nacimiento']
        grado = request.form['grado']

        # archivo a enviar
        imagen = request.files['imagen']

        payload = {
            "PrimerNombre": primerNombre,
            "SegundoNombre": segundo_nombre,
            "PrimerApellido": primer_apellido,
            "SegundoApellido": segundo_apellido,
            "FechaDeNacimiento": fecha_nacimiento,
            "GradoCursante": grado,
        }

        files = [('FotoDelEstudiante', (imagen.filename, imagen.stream, imagen.mimetype))]
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        data = response.json()
        print(data)

        return redirect("/informacion")

    return render_template('inscribir.html')


@app.route("/informacion", methods=['POST', 'GET'])
def informacion():
    """Podemos ver la lista de estudiantes"""
    response = requests.request("GET", url, headers=headers)
    data = response.json()

    return render_template('informacion.html', data=data)


@app.route("/actualizar/<int:id>", methods=['POST', 'GET'])
def actualizar(id):
    """Podemos actualizar los estudiantes"""
    response = requests.request("GET", url + str(id), headers=headers)
    data = response.json()
    if request.method == 'POST':
        primerNombre = request.form['primer_nombre']
        segundo_nombre = request.form['segundo_nombre']
        primer_apellido = request.form['primer_apellido']
        segundo_apellido = request.form['segundo_apellido']
        fecha_nacimiento = request.form['fecha_nacimiento']
        grado = request.form['grado']

        # archivo a enviar
        imagen = request.files['imagen']

        payload = {
            "PrimerNombre": primerNombre,
            "SegundoNombre": segundo_nombre,
            "PrimerApellido": primer_apellido,
            "SegundoApellido": segundo_apellido,
            "FechaDeNacimiento": fecha_nacimiento,
            "GradoCursante": grado,
            # "FotoDelEstudiante":
        }

        files = [('FotoDelEstudiante', (imagen.filename, imagen.stream, imagen.mimetype))]
        response = requests.request("PUT", url + str(id) + "/", headers=headers, data=payload, files=files)
        data = response.json()
        print(data)
        return redirect("/informacion")

    # Realizar alguna acción específica para el ID proporcionado
    return render_template('actualizar.html', data=data)


@app.route("/eliminar/<int:id>", methods=['POST', 'GET'])
def eliminar(id):
    """Eliminar los estudiantes de manera sencilla"""
    requests.request("DELETE", url + str(id) + "/", headers=headers)
    return redirect("/informacion")


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    """Contener errores"""
    return 'Pagina no encontrada', 400


@app.errorhandler(404)
def page_not_found(e):
    """Para que no accedan a rutas no creadas"""
    return 'Pagina no encontrada', 404


if __name__ == "__main__":
    app.run(port=7000)
