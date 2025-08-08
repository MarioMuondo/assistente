import speech_recognition as sr

def listen_from_mic(timeout=5, phrase_time_limit=6):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ajustando ruído ambiente...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Fale agora...")
        audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    try:
        # Usando Google Web Speech API (requer internet)
        text = r.recognize_google(audio, language="pt-PT")  # "pt-BR" ou "pt-PT"
        print("Você disse:", text)
        return text
    except sr.UnknownValueError:
        print("Não entendi o áudio.")
        return ""
    except sr.RequestError as e:
        print("Erro na API de reconhecimento; ", e)
        return ""
