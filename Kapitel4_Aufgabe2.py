N = 2

print("Erste Matrix:")
zeile = list() #leere Liste erzeugen
matrix = list() #leere Liste erzeugen
for i in range(1, N + 1):
    for j in range(1,N + 1):
        print("Element [",i,"][",j,"] eingeben: ")
        zeile.append(int(input()))
    matrix.append(zeile) #fertige Zeile hinzufügen
    zeile = list() #leere Zeile erzeugen

print("Zweite Matrix:")
matrix2 = list() #leere Liste erzeugen
for i in range(1, N + 1):
    for j in range(1,N + 1):
        print("Element [",i,"][",j,"] eingeben: ")
        zeile.append(int(input()))
    matrix2.append(zeile) #fertige Zeile hinzufügen
    zeile = list() #leere Zeile erzeugen

print(matrix, end = " * ")
print(matrix2)

ergebnis = list()
zeile = list()
zeile.append((matrix[0][0] * matrix2[0][0]) + (matrix[0][1] * matrix2[1][0]))
zeile.append((matrix[0][0] * matrix2[0][1]) + (matrix[0][1] * matrix2[1][1]))
ergebnis.append(zeile)
zeile = list()
zeile.append((matrix[1][0] * matrix2[0][0]) + (matrix[1][1] * matrix2[1][0]))
zeile.append((matrix[1][0] * matrix2[0][1]) + (matrix[1][1] * matrix2[1][1]))
ergebnis.append(zeile)
print(ergebnis)
