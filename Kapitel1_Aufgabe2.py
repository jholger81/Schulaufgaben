# I = U/R

print("Stromstärkeberechnung Version 1.0")
print("Bitte geben Sie die Spannung in Volt ein:")
spannung = int(input())
print("Bitte geben Sie den Widerstand in Ohm ein:")
widerstand = float(input())
stromstärke = spannung / widerstand
print("Die Stromstärke lautet: ", stromstärke)
