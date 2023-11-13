nummern = 1
vorige = 0
print (nummern)
while nummern < 255:
    nummern = vorige + nummern
    vorige = nummern 
    print(nummern)