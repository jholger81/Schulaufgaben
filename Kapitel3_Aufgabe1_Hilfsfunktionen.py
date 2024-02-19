def Zerlege(zahl):
    x = int(zahl/100)
    y = int((zahl-x*100)/10)
    z = int(zahl-x*100-y*10)
    return x, y, z