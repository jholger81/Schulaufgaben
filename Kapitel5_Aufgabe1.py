class Dreieck:
    def __init__(self, a, b, c):
        if ((a*a + b*b) == (c*c)):
            self.__a = a
            self.__b = b
            self.__c = c
        else:
            self.__a = 3
            self.__b = 4
            self.__c = 5
    
    def Ausgabe(self):
        print("Die Seiten des Dreiecks lauten: ", end = "")
        print(self.__a, end = " ")
        print(self.__b, end = " ")
        print(self.__c)
        
    def Seiten(self):
        mytuple = (self.__a, self.__b, self.__c)
        return mytuple
    
d_1 = Dreieck(1, 2, 3)
d_2 = Dreieck(6, 8, 10)
d_1.Ausgabe()
d_2.Ausgabe()
print(d_1.Seiten())
print(d_2.Seiten())