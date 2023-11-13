bestelling = {}
prijskaart = {
    "worstenbrood": 1.5,
    "cola": 1,
    "geld": 50
}
ding = ""
print("Wa wilde hebben?")
ding = input()
while ding != "":
    if ding in bestelling and (ding.lower() == "worstenbrood" or ding.lower() == "cola" or ding.lower() == "geld"):
        bestelling[ding.lower()] += 1 
        print("Nog iet?")
        ding = input()
    elif ding.lower() == "worstenbrood" or ding.lower() == "cola" or ding.lower() == "geld":
        bestelling[ding.lower()] = 1
        print("Nog iet?")
        ding = input()
    else:
        print("ALLEE DA GE NIE EH")    
for ding in bestelling:
    print(ding + ":", bestelling[ding])
for besteld in bestelling:
    print(ding + ":", prijskaart[ding]*bestelling[ding], "euro")
print("Totaal:", (prijskaart["worstenbrood"]*bestelling["worstenbrood"])+(prijskaart["cola"]*bestelling["cola"])+(prijskaart["geld"]*bestelling["geld"]), "euro")

