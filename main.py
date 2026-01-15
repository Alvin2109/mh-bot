import time
import os  # Importante para leer las llaves secretas
from vinted_scraper import VintedScraper
import requests

# --- CONFIGURACIÓN SEGURA ---
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
# ----------------------------

scraper = VintedScraper("https://www.vinted.es")
vistos = set()

print("¡Buscador seguro activado!")

while True:
    try:
        items = scraper.search("https://www.vinted.es/catalog?search_text=monster%20high&order=newest_first")
        
        if items:
            for item in items[:5]:
                if item.id not in vistos:
                    mensaje = f"📸 ¡NUEVA MH!\n💰 Precio: {item.price}€\n🔗 Link: {item.url}"
                    url_tg = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={mensaje}"
                    requests.get(url_tg)
                    vistos.add(item.id)
        
        time.sleep(600) # 4 minutos para evitar bloqueos
        
    except Exception as e:
        print(f"Aviso: {e}")
        time.sleep(300)
