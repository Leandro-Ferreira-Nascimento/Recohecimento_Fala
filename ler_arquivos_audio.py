import speech_recognition as sr

# esse é no recognizer
rec = sr.Recognizer()

# lendo o arquivo de audio
with sr.AudioFile("teste.wav") as arquivo_audio:
    audio = rec.record(arquivo_audio)
    texto = rec.recognize_google(audio, language="en")
    print(texto)
