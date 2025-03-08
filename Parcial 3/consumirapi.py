import requests
import json

#url = "http://127.0.0.1:5000/tasks"
url = "https://jsonplaceholder.typicode.com/todos"
#url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print('Solicitud Existosa')
    print("Datos: ", data)

    with open('datos.json', 'w') as archivo_json:
        json.dump(data, archivo_json, indent=4)
    print("Los datos han sido guardados en 'datos.json")
else:
    print("Error en la solicitud: ", response.text)
