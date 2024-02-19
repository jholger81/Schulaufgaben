originalPW1 = "P"
originalPW2 = "R"
originalPW3 = "O"
originalPW4 = "G"
count = 1
correct1 = False
correct2 = False
correct3 = False
correct4 = False

while count <=3:
    print("Versuch NR. ", count)
    zeichen1 = input("Bitte das erste Zeichen eingeben:")
    zeichen2 = input("Bitte das zweite Zeichen eingeben:")
    zeichen3 = input("Bitte das dritte Zeichen eingeben:")
    zeichen4 = input("Bitte das vierte Zeichen eingeben:")
    if originalPW1 == zeichen1 or originalPW1 == zeichen2 or originalPW1 == zeichen3 or originalPW1 == zeichen4:
        correct1 = True
    if originalPW2 == zeichen1 or originalPW2 == zeichen2 or originalPW2 == zeichen3 or originalPW2 == zeichen4:
        correct2 = True
    if originalPW3 == zeichen1 or originalPW3 == zeichen2 or originalPW3 == zeichen3 or originalPW3 == zeichen4:
        correct3 = True
    if originalPW4 == zeichen1 or originalPW4 == zeichen2 or originalPW4 == zeichen3 or originalPW4 == zeichen4:
        correct4 = True
    if correct1 and correct2 and correct3 and correct4:
        print("Login korrekt!")
        break
    correct1 = False
    correct2 = False
    correct3 = False
    correct4 = False
    count += 1
if count >=4:
    print("Keine Versuche ueber")
    
