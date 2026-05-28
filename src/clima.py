import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()


def get_clima(ciudad: str) -> dict:
    """Obtiene el clima actual de una ciudad usando la API de OpenWeather.

    Args:
        ciudad (str): Nombre de la ciudad a consultar.

    Returns:
        dict: Datos del clima devueltos por la API.
    """
    print("Buscando en caché...")
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("BASE_URL")
    units = os.getenv("UNITS")

    # Reemplaza esto con la lógica real de tu API si es necesario
    params = {"q": ciudad, "appid": api_key, "units": units}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    return {"error": "No se pudo obtener el clima"}
