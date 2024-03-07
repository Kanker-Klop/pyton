from time import sleep

x = {
    1: [True, False, False, False, True],
    2: [False, True, False, True, False],
    3: [False, False, True, False, False],
    4: [False, True, False, True, False],
    5: [True, False, False, False, True]
}

pluspat = {
    1: [False, False, True, False, False],
    2: [False, False, True, False, False],
    3: [True, True, True, True, True],
    4: [False, False, True, False, False],
    5: [False, False, True, False, False]
}

y = {
    1: [True, False, False, False, True],
    2: [False, True, False, True, False],
    3: [False, False, True, False, False],
    4: [False, False, True, False, False],
    5: [False, False, True, False, False]
}

t = {
    1: [True, True, True, True, True],
    2: [False, False, True, False, False],
    3: [False, False, True, False, False],
    4: [False, False, True, False, False],
    5: [False, False, True, False, False]

}

for kaka in range(1):
    for ypsilon in range(1,6):
        for ypsilonnen in range(5):
            print(y[ypsilon][ypsilonnen])
            flakkapis = ypsilonnen+5
            print(flakkapis)
            sleep(0.0000001)
sleep(0.1)
print("SCHEIDING\n")

for pipi in range(1):
    for plus in range(1,6):
        for plussen in range(5):
            print(pluspat[plus][plussen])
            sleep(0.0000001)
sleep(0.1)
print("SCHEIDING\n")

for kots in range(2):
    for tee in range(1,6):
        for tees in range(5):
            print(t[tee][tees])
            sleep(0.0000001)
sleep(0.1)
print("SCHEIDING\n")
