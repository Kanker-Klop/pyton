def kanker_op():
    #Deze functie zegt gewoon kanker op
    print("kanker op")
kanker_op()

def kwadrateer(getal):
    kwadraat = pow(getal, 2)
    return kwadraat
amai = kwadrateer(69)
print(amai)

kanker = kwadrateer(4761)
print(kanker)

def naamvanu():
    print("Wa is votre nom")
    naam = input()
    print("Uw naam is", naam)
naamvanu()

def tetratiemoeder(getal,tet):
    getetreerd = getal
    for amai in range(0,tet,1):
        getetreerd = getetreerd**getal
    return getetreerd
    
print(tetratiemoeder(2,4))