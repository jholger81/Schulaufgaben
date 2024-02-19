def ToList(zeichenkette):
    liste = []
    for i in range (0,len(zeichenkette),1):
        liste.append(zeichenkette[i])
    return liste
        
def ToUpper(inputListe):
    for i in range (0,len(inputListe),1):
        if ord(inputListe[i]) > 96 and ord(inputListe[i]) < 123: # lower case letters
            inputListe[i] = chr(ord(inputListe[i]) - 32)
    return inputListe




count = 1
passwort = "PROGRAMMIEREN"
# passwort = "prOgrammieren"
pwlist = ToList(passwort)
pwlist = ToUpper(pwlist)
pwlist.sort()
pwcorrect = False

while count <=3:
    print("Versuch NR. ", count)
    eingabe = input("Passwort eingeben:")
    eingabelist = ToList(eingabe)
    eingabelist = ToUpper(eingabelist)
    eingabelist.sort()
    if len(pwlist) != len(eingabelist):
        pwcorrect = False
        count += 1
        continue
    for i in range (0, len(pwlist), 1):
        if pwlist[i] != eingabelist[i]:
            pwcorrect = False
            count += 1
            break
        else:
            pwcorrect = True
    if pwcorrect:
        break
if not pwcorrect:
    print("Keine Versuche ueber")
else:
    print("Passwort korrekt")
    
