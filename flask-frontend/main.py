import requests


def obtener_token(username, password):
    # URL de la API de autenticación
    url = "http://127.0.0.1:8000/api/token/"

    # Credenciales de inicio de sesión
    payload = {"username": username, "password": password}

    # Realizar la solicitud HTTP POST a la API de autenticación
    response = requests.post(url, data=payload)

    # Verificar el código de estado de la respuesta
    if response.status_code == 200:
        # Extraer el token JWT del cuerpo de la respuesta
        token = response.json().get("access")
        return token
    else:
        # Si la solicitud falla, lanzar una excepción con el mensaje de error
        raise Exception("Error al obtener el token: {}".format(response.text))


token = obtener_token('user', 'pasword')  # función para obtener el token JWT válido


def post_datos(datos, token):
    # Crear el encabezado de autorización con el token JWT
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    # Hacer una solicitud GET a la API protegida con el encabezado de autorización
    response = requests.post('http://127.0.0.1:8000/api/estudiantes/', data=datos, headers=headers)
    return response.json()


if __name__ == "__main__":
    pass
