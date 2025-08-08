import pyttsx3

_engine = None

def init_tts(rate=150, volume=1.0, voice_id=None):
    global _engine
    _engine = pyttsx3.init()
    _engine.setProperty('rate', rate)
    _engine.setProperty('volume', volume)
    if voice_id:
        _engine.setProperty('voice', voice_id)

def speak(text):
    global _engine
    if _engine is None:
        init_tts()
    _engine.say(text)
    _engine.runAndWait()
