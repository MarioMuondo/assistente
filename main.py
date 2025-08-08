from stt import listen_from_mic
from tts import init_tts, speak
from nlp_intent import get_intent_and_entities
from actions import action_wikipedia, action_open_youtube, action_find_pharmacy

def main():
    init_tts()
    speak("Olá! Assistente pronta. Em que posso ajudar?")
    while True:
        text = listen_from_mic()
        if not text:
            speak("Não entendi. Pode repetir?")
            continue

        intent, ents = get_intent_and_entities(text)

        if intent == "wikipedia_search":
            resp = action_wikipedia(ents.get("topic"))
            speak(resp)
        elif intent == "open_youtube":
            resp = action_open_youtube(ents.get("query"))
            speak(resp)
        elif intent == "find_pharmacy":
            resp = action_find_pharmacy()
            speak(resp)
        elif intent == "greeting":
            speak("Olá! Em que posso ajudar?")
        elif intent == "exit":
            speak("Até logo!")
            break
        else:
            speak("Desculpe, não sei realizar essa ação ainda.")

if __name__ == "__main__":
    main()
