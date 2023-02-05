import speech_recognition as sr

a = sr.Recognizer()
sentence = sr.AudioFile('audio.wav')

with sentence as source:
    audio = a.record(source)
    
a.recognize_google(audio)