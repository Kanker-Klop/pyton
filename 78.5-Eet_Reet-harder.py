NamenAmen = []
new = input('new name: ')
while new != '':
    idx = 0
    for name in NamenAmen:
        if name > new:
            break
        idx += 1
    NamenAmen.insert(idx, new)
    new = input('nog een naam: ')
print(NamenAmen)