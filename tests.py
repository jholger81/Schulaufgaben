from math import pi, cos

def lokal_global():
    print("lokal: ", global_x)

global_x = 10
print("global: ", global_x)
lokal_global()
print("Pi:", pi)
# print("Pi:", math.pi) // wuerde nur mit import math funltionieren
