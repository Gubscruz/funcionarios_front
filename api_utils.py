import requests


BASE_URL = "http://127.0.0.1:4800"

def get_problemas():
    response = requests.get(f'{BASE_URL}/problemas')
    return response.json()

def mostra_problemas_filtrado():
    try:
        response = requests.get(f"{BASE_URL}/problemas/filter")
        response.raise_for_status()
        return True, response.json()
    except Exception as e:
        return False, {"message": str(e)}
    
