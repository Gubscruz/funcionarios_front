import requests


BASE_URL = "https://reporta-cidade-36c5016e43fd.herokuapp.com"

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
    

    
