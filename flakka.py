jaNee = "wollah"
print("WE GON DELEN, GAST")
print("KOM, GEEFT IS UW EERSTE GETAL")
getal1 = float(input())
print("EN NÀ DEN TWEEDE")
getal2 = float(input())
if getal2 == 0:
    print("ALLEI GAST, DA GO NIE EH! WILDE MISSCHIEN BETER DOOR EEN GETAL DA NIE NUL IS DELEN????")
    jaNee = input()
    while jaNee == "Nee" or jaNee == "nee" or jaNee == "ne" or jaNee == "Ne":
        print("ALLEIIIIIIIIIIIII, PLEASE?")
        jaNee = input()
    print("ALLEI, GEEFT DAN IS IET DA NIE 0 IS")
    getal2 = float(input())
uitkomst = getal1 / getal2
print("AMAI, ZENNE! " + str(getal1) + " GEDEELD DOOR " + str(getal2) + " IIIIIS: " + str(uitkomst))