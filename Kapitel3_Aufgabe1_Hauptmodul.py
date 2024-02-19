import Kapitel3_Aufgabe1_Aussprache
import Kapitel3_Aufgabe1_Hilfsfunktionen

gueltig = False

while (not gueltig):
    eingabe = input("Zahl eingeben, maximal 3 Stellen: ")
    try:
        x = int(eingabe)
    except ValueError:
        print("Eingabe ist keine Zahl!")
        continue
    if (x >= 1000):
        print("Zahl muss zwischen 0 und 999 liegen")
        continue
    gueltig = True
print("Eingabe gueltig, aussprache der Zahl ", x, ":")
Kapitel3_Aufgabe1_Aussprache.Aussprache(x)


for i in range(1, 999, 1):
    Kapitel3_Aufgabe1_Aussprache.Aussprache(i)
    #input("")
    