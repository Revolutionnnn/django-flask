import requests
import json
# Este archivo lo utilice para hacer pruebas a la API
url = "http://127.0.0.1:8000/api/estudiantes/"

# payload={'PrimerNombre': 'Pepito',
# 'SegundoNombre': 'Alverto',
# 'PrimerApellido': 'Perez',
# 'SegundoApellido': 'Pereira',
# 'FechaDeNacimiento': '2023-02-15',
# 'GradoCursante': '1'}
# files=[
#   ('FotoDelEstudiante',('password.png',open('a.png','rb'),'image/png'))
# ]
headers = {
  'Authorization': 'Bearer TOKEN JWT'
}
response = requests.request("GET", url + '1', headers=headers)
data = response.json()
print(data)
