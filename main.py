import time
from vinted_scraper import VintedScraper
import requests

# --- CONFIGURACIÓN ---
TOKEN = "7687197350:AAGeoKxVh3mZMP0LQqXzManQHWpPFtlxgec"
CHAT_ID = "-1003626300588"
# ---------------------

# Arreglo del error: Usamos la URL completa del dominio
scraper = VintedScraper("https://www.vinted.es")
vistos = set()

print("¡Buscador corregido y activado!")

while True:
    try:
        # Buscamos Monster High ordenado por lo más nuevo
        items = scraper.search("https://www.vinted.es/catalog?search_text=monster%20high&order=newest_first")
        
        if items:
            for item in items[:5]:
                if item.id not in vistos:
                    mensaje = f"📸 ¡NUEVA MH!\n💰 Precio: {item.price}€\n🔗 Link: {item.url}"
                    url_tg = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={mensaje}"
                    requests.get(url_tg)
                    vistos.add(item.id)
                    print(f"Anuncio detectado: {item.id}")
        
        time.sleep(120) 
        
    except Exception as e:
        print(f"Aviso: {e}. Reintentando...")
        time.sleep(60)
