import webbrowser
import wikipedia

from geopy.geocoders import Nominatim
import geocoder  # para IP-based geolocation
from urllib.parse import quote_plus

wikipedia.set_lang("pt")

def action_wikipedia(topic):
    if not topic:
        return "Sobre o quê deseja pesquisar na Wikipédia?"
    try:
        summary = wikipedia.summary(topic, sentences=2)
        url = wikipedia.page(topic).url
        return f"{summary} \nMais em: {url}"
    except Exception as e:
        return f"Não encontrei informações sobre {topic} na Wikipédia. ({e})"

def action_open_youtube(query):
    if not query:
        webbrowser.open("https://www.youtube.com")
        return "Abrindo YouTube."
    q = quote_plus(query)
    webbrowser.open(f"https://www.youtube.com/results?search_query={q}")
    return f"Abrindo resultados do YouTube para {query}."

def action_find_pharmacy():
    # tentativa simples de localização por IP (impreciso) — para demo
    g = geocoder.ip('me')
    if not g.ok or not g.latlng:
        return "Não consegui obter sua localização automática. Poderia fornecer a sua cidade?"
    lat, lng = g.latlng
    geolocator = Nominatim(user_agent="my_assistant")
    location = geolocator.reverse((lat, lng), language='pt')
    city = None
    if 'city' in location.raw['address']:
        city = location.raw['address']['city']
    elif 'town' in location.raw['address']:
        city = location.raw['address']['town']
    place_query = f"farmácia em {city}" if city else "farmácia próxima"
    # abrir mapa com pesquisa
    webbrowser.open(f"https://www.google.com/maps/search/{quote_plus(place_query)}")
    return f"Abrindo no mapa: {place_query} (baseado em localização aproximada)."
