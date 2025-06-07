import requests

BASE_URL = "http://localhost:8000/api"

def login(username: str, password: str):
    response = requests.post(
        f"{BASE_URL}/login",
        data={"username": username, "password": password}
    )
    
    if response.status_code == 200:
        token = response.json().get("access_token")
        print("Login exitoso!")
        return token
    else:
        print("Error al iniciar sesión:", response.json().get("detail"))
        return None

def get_profile(token: str):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/profile", headers=headers)
    
    if response.status_code == 200:
        print("Perfil del usuario:")
        print(response.json())
    else:
        print("Error al obtener el perfil:", response.json().get("detail"))

if __name__ == "__main__":
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    
    token = login(username, password)
    
    if token:
        get_profile(token)
