naam = input("zegt is wa uw naam is: ").strip()
leeftijd = input ("zegt ook is uwe leeftijd: ")
while leeftijd.isnumeric() == False:
    leeftijd = input("allee, geeft gewoon uwe leeftijd is: ")
print("Deze knuppel heet", naam, "en is", leeftijd, "jaren oud")