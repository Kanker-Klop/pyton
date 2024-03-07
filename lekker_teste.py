from time import sleep
import random
while True:
    kaka1 = 2+random.randint(0,30)
    kaka2 = 5+random.randint(0,27)
    kaka3 = random.randint(0,32)
    sleep(0.005)
    kakpis = (kaka1 == kaka2 == kaka3)
    print(kakpis)
    if kakpis:
        sleep(1)