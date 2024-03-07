import random
from time import sleep


print("Kom, we gon is fnaf nadoen")

Bonnie = int(input("Geeft is den AI level van Bonnie (tussen 0 en 20): "))
Chica = int(input("Geeft is den AI level van Chica (tussen 0 en 20): "))
Freddy = int(input("Geeft is den AI level van Freddy (tussen 0 en 20): "))
Foxy = int(input("Geeft is den AI level van Foxy (tussen 0 en 20): "))

foxyStatus = 0
while True:
    bonnieBeweeg = random.randint(0,20)
    if Bonnie >= bonnieBeweeg:
        print("Bonnie heeft bewogen")
    sleep(4.97)
    chicaBeweeg = random.randint(0,20)
    if Chica >= bonnieBeweeg:
        print("Chica heeft bewogen")
    sleep(4.97)
    freddyBeweeg = random.randint(0,20)
    if Freddy >= freddyBeweeg:
        print("Freddy heeft bewogen")
    sleep(2.97)
    foxyBeweeg = random.randint(0,20)
    if foxyStatus == 4:
        print("Foxy komt voor uw reet")
        break
    elif Foxy >= foxyBeweeg:
        foxyStatus = foxyStatus+1
    sleep(1.97)
print("Dood, lol")