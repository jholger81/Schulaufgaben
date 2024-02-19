from ast import If
import Kapitel3_Aufgabe1_Hilfsfunktionen
from gtts import gTTS
import os

def Aussprache(x):
    stelle100, stelle10, stelle1 = Kapitel3_Aufgabe1_Hilfsfunktionen.Zerlege(x)
    DoIt(stelle100, stelle10, stelle1)

def SprecheZahl(zahl):
    if(zahl == 1):
        print("ein", end = '')
    if(zahl == 2):
        print("zwei", end = '')    
    if(zahl == 3):
        print("drei", end = '')
    if(zahl == 4):
        print("vier", end = '')
    if(zahl == 5):
        print("fuenf", end = '')
    if(zahl == 6):
        print("sechs", end = '')
    if(zahl == 7):
        print("sieben", end = '')
    if(zahl == 8):
        print("acht", end = '')
    if(zahl == 9):
        print("neun", end = '')
    if(zahl == 0):
        print("null", end = '')

def SprecheZahlZehner(zahl):
    if(zahl == 1):
        print("zehn", end = '')
    if(zahl == 2):
        print("zwanzig", end = '')
    if(zahl == 3):
        print("dreissig", end = '')
    if(zahl == 6):
        print("sechzig", end = '')
    if(zahl == 7):
        print("siebzig", end = '')
    if(zahl not in (1, 2, 3, 6,7)):
        SprecheZahl(zahl)
        print("zig", end = '')

def SprecheZahlEiner(zahl):
    SprecheZahl(zahl)

def Spreche100(zahl):
    SprecheZahl(zahl)
    print("hundert", end = '')

def Spreche10(zahl):
    SprecheZahlZehner(zahl)

def Spreche1(zahl):
    if (zahl > 0):
        SprecheZahl(zahl)
    
def SprecheSonderfall(zahl):
    if(zahl == 1):
        print("elf", end = '')
    if(zahl == 2):
        print("zwoelf", end = '')
    if(zahl == 6):
        print("sechzehn", end = '')
    if(zahl == 7):
        print("siebzehn", end = '')

def DoIt(stelle100, stelle10, stelle1):
    if (stelle100>0):
        Spreche100(stelle100)
        if ((stelle10 > 0 or stelle1 > 0)):# and stelle100 > 0):
            print(" und ", end = '')
    if (stelle10 > 0):
        if (stelle10 == 1 and stelle1 in (1, 2, 6, 7)):
            SprecheSonderfall(stelle1)
            print("")
            return
        else:
            Spreche1(stelle1)
            if (stelle10 > 1 and stelle1 > 0):
                print(" und ", end = '')
            
            Spreche10(stelle10)
    if (stelle1 > 0 and stelle10 == 0):
        SprecheZahlEiner(stelle1)
        if (stelle1 == 1):
            print("s", end = '')
    print("")    
    text_to_speech("einhundert drei und dreissig")

def text_to_speech(text):
    speech = gTTS(text)
    speech_file = 'speech.mp3'
    speech.save(speech_file)
    os.system('afplay ' + speech_file)