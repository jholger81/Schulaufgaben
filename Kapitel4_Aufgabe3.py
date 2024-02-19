basisline = {"weiss", "blau", "schwarz", "rot", "silber-metallic"}
upline = {"blau", "schwarz-metallic", "silber-metallic", "grau-metallic"}
highline = {"rot", "schwarz-metallic", "silber-metallic", "grau-metallic", "cremeweiss"}
luxline = {"schwarz-metallic", "silber-metallic", "grau-metallic", "cremeweiss", "hellgrau", "silbergrau"}
modelListe = [basisline, upline, highline, luxline]

def Menu():
    eingabe = -1
    while eingabe < 0 or eingabe > 4:
        print("1. Farbe hinzufuegen")
        print("2. Anzahl Farben aller Modelle ausgeben")
        print("3. Farben ausgeben, die nur in der Luxline vorhanden sind")
        print("4. Farben ausgeben, die in allen Varianten vorhanden sind")
        print("0. Programm beenden")
        print("Auswahl:", end = "")
        try:
            eingabe = int(input())
        except ValueError:
            return -1
    return eingabe

def FarbeHinzufuegen():
    print("Fuer welches Modell soll eine Farbe hinzugefuegt werden")
    print("1: Basisline")
    print("2: Upline")
    print("3: Highline")
    print("4: Luxline")
    print("Auswahl:", end = "")
    try:
        auswahl = int(input())
    except ValueError:
        return
    if(auswahl not in (1, 2, 3, 4)):
        return
    print("Farbe:", end = "")
    farbe = input()
    if(auswahl == 1):
        basisline.add(farbe)
    if(auswahl == 2):
        upline.add(farbe)
    if(auswahl == 3):
        highline.add(farbe)
    if(auswahl == 4):
        luxline.add(farbe)

def FarbenAausgebenAnzahlAlleModelle():
    count = 0
    for i in range(0, len(modelListe), 1):
        for j in range(0, len(modelListe[i]), 1):
            count += 1
    farben = len(basisline | upline | highline | luxline)
    print("Anzahl Farb-Modell-Variationen gesamt:", count)
    print("Anzahl verschiedener Farben:", farben)
    
def FarbenAusgebenLuxline():
    ergebnis = luxline - highline - upline - basisline
    print("Farben, die ausschliesslich in der Luxline vorhanden sind: ", ergebnis)

def FarbenAusgebenAlleModelle():
    ergebnis = luxline & highline & upline & basisline
    print("Farben, die in allen Varianten vorhanden sind: ", ergebnis)


auswahl = -1
while auswahl != 0:
    auswahl = Menu()
    if(auswahl == 1):
        FarbeHinzufuegen()
    if(auswahl == 2):
        FarbenAausgebenAnzahlAlleModelle()
    if(auswahl == 3):
        FarbenAusgebenLuxline()
    if(auswahl == 4):
        FarbenAusgebenAlleModelle()