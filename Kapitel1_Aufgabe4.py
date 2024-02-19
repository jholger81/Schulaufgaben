def do_stuff(zahl1, zahl2):
    while (zahl1 > zahl2):
        zahl1 -= zahl2
    return zahl1

print("Modulo ohne % - Version 1.0")
print("Bitte geben Sie die erste Zahl ein:")
zahl1 = int(input())
print("Bitte geben Sie die zweite Zahl ein:")
zahl2 = float(input())
rest = int (do_stuff(zahl1, zahl2))
print("Rest: ", rest)
