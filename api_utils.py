import requests


BASE_URL = "http://127.0.0.1:4800"

def get_problemas():
    try:
        response = requests.get(f'{BASE_URL}/problemas')
        return True, response.json()
    except Exception as e:
        return False, {"message": str(e)}

def mostra_problemas_filtrado(filtro):
    try:
        response = requests.get(f"{BASE_URL}/problemas/filter", json={"urgencia": filtro})
        response.raise_for_status()
        return True, response.json()
    except Exception as e:
        return False, {"message": str(e)}
    
def update_problemas(problema):
    try:
        response = requests.put(f"{BASE_URL}/problemas", json=problema)
        response.raise_for_status()
        return True, response.json()
    except Exception as e:
        return False, {"message": str(e)}
    

    
