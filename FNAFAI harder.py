import random, threading
from time import sleep

def Bonnie(AI_level):
    while True:
        lekker_random = random.randint(1,20)
        if AI_level >= lekker_random:
            print("Bonnie heeft bewogen")
        sleep(3.97)

def Chica(AI_level):
    while True:
        lekker_random = random.randint(1,20)
        if AI_level >= lekker_random:
            print("Chica heeft bewogen")
        sleep(3.97)

def Freddy(AI_level):
    while True:
        lekker_random = random.randint(1,20)
        if AI_level >= lekker_random:
            print("Freddy heeft bewogen")
        sleep(4.97)

def foxy(AI_levele):
    print("jamajezus")


print("Kom, we gon is fnaf nadoen")

Bonbon = int(input("Geeft is den AI level van Bonnie (tussen 0 en 20): "))
Chicken = int(input("Geeft is den AI level van Chica (tussen 0 en 20): "))
Alfredo = int(input("Geeft is den AI level van Freddy (tussen 0 en 20): "))
Foxy = int(input("Geeft is den AI level van Foxy (tussen 0 en 20): "))

bonniebestaan = threading.Thread(target=Bonnie(Bonbon))
chicabestaan = threading.Thread(target=Chica(Chicken))
freddybestaan = threading.Thread(target=Freddy(Alfredo))

bonniebestaan.start(), chicabestaan.start(), freddybestaan.start()