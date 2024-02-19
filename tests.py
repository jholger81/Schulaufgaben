# from math import pi, cos

# def lokal_global():
#     print("lokal: ", global_x)

# global_x = 10
# print("global: ", global_x)
# lokal_global()
# print("Pi:", pi)
# # print("Pi:", math.pi) // wuerde nur mit import math funltionieren



class Person:
    anzahl_instanzen = 0
    
    def __init__(self):
        self.__name = "leer"
        Person.anzahl_instanzen += 1
    
p1 = Person()
p2 = Person()
p3 = Person()
print(Person.anzahl_instanzen)
print(p1.anzahl_instanzen)
Person.anzahl_instanzen += 1
print(Person.anzahl_instanzen)
print(p1.anzahl_instanzen)