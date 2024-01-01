import speech_recognition as sr
import webbrowser
import time
from datetime import datetime
import playsound
from gtts import gTTS
import random
import os


r= sr.Recognizer()

def record(ask=False):


    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio= r.listen(source)
        voice=''
        try:
            voice = r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError:
            print('Anlayamadım')
        except sr.RequestError:
            print('Sistem Çalışmıyor.')
        return voice
    
def response(voice):
    if 'nasılsın' in voice:
        speak('iyi senden naber')
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        search = record('ne aramak istiyorsun')
        url ='https://google.com/search?q='+search
        webbrowser.get().open(url)
    if 'tamamdır'in voice:
        speak('Görüşmek üzere')
        exit()
        
def speak(string):
    tts = gTTS(string,lang='tr')
    rand = random.randint(1,100000)
    file="audio-"+str(rand)+'.mp3' 
    tts.save(file) 
    playsound(file)
    os.remove(file)    
          
speak('Nasıl yardımcı olabilirim')
time.sleep(1)
while 1:
    voice=record()
    print(voice)
    response(voice)
