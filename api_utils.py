import requests

BASE_URL = "http://127.0.0.1:4800"

def get_problemas():
    response = requests.get(BASE_URL + "/problemas")
    return response.json()