import math

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def entfernung(self, p2):
        d = math.sqrt(((p2.x-self.x)**2) + ((p2.y - self.y)**2))
        return d
    
    def __eq__(self, p2):
        if((self.x == p2.x) and (self.y == p2.y)):
            return True
        else:
            return False
        
    def __lt__(self, p2):
        ursprung = Punkt(0.0, 0.0)
        if((self.entfernung(ursprung)) < (p2.entfernung(ursprung))):
            return True
        else:
            return False
        
    def __gt__(self, p2):
        ursprung = Punkt(0.0, 0.0)
        if((self.entfernung(ursprung)) > (p2.entfernung(ursprung))):
            return True
        else:
            return False

    def __float__(self):
        ursprung = Punkt(0.0, 0.0)
        dist = self.entfernung(ursprung)
        return dist
    
    def __str__(self):
        mystring = "P(" + str(self.x) + "," + str(self.y) + ")"
        return mystring
    
    def __call__(self, x, y):
        self.x = x
        self.y = y
   


p1 = Punkt(1.0, 2.0)
print(p1)

p2 = Punkt(3.0, 4.0)
print(p2)
print(float(p1))
print(float(p2))

print(p1 < p2)
print(p1 > p2)
print(p1 == p2)

p1(3.0, 4.0)
print(p1 == p2)