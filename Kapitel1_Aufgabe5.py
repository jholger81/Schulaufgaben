weiche1 = int(input("Weichenstellung 1:"))
weiche2 = int(input("Weichenstellung 2:"))
weiche3 = int(input("Weichenstellung 3:"))
print("Der Zug fährt ein in Bahnhof: ", weiche1&weiche2 or ~weiche1&weiche3 or weiche1&~weiche2&weiche3)