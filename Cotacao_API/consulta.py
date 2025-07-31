import os 
from dotenv import load_dotenv
import requests

load_dotenv()  # Carrega as variáveis do arquivo .env


API_KEY = os.getenv("API_KEY")
url = requests.get(f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD")

moedas = url.json()

for moeda in moedas['conversion_rates']:
    print(f"{moeda}: {moedas['conversion_rates'][moeda]}")  