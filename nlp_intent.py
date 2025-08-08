import re

def get_intent_and_entities(text):
    t = text.lower()

    # intenções simples por palavras-chave
    if "wikipedia" in t or "pesquisa" in t and "wikipedia" in t:
        # extrair tópico
        m = re.search(r'(?:wikipedia|pesquise|pesquisa)\s+(sobre\s+)?(.+)', t)
        topic = m.group(2) if m else ""
        return ("wikipedia_search", {"topic": topic.strip()})

    if "youtube" in t or "vídeo" in t:
        m = re.search(r'(?:youtube|vídeo)\s+(de|sobre)?\s*(.+)', t)
        topic = m.group(2) if m else ""
        return ("open_youtube", {"query": topic.strip()})

    # procurar farmácia mais próxima
    if "farmácia" in t or "farmacia" in t:
        return ("find_pharmacy", {})

    if "parar" in t or "sair" in t or "fechar" in t:
        return ("exit", {})

    # fallback: small talk
    if "olá" in t or "oi" in t:
        return ("greeting", {})

    return ("unknown", {})
