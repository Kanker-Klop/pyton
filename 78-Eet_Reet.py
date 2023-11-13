NamenAmen = []
print("geeft is ne naam fso")
nenaam = input()
NamenAmen.append(nenaam)
while nenaam != "":
    print("geeft nog ne naam?")
    nenaam = input()
    if nenaam == "":
        break
    else:
        NamenAmen.append(nenaam)
        NamenAmen.sort()
print(NamenAmen)