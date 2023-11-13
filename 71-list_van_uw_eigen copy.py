print("Geeft is dingen da ge in een lijst wilt")
wjwlijst = []
Nogiet = input()
while Nogiet != "":
    wjwlijst.append(Nogiet)
    print("Geeft nog iets, als ge klaar zijt doe dan gewoon enter")
    Nogiet = input()
print ("Ge hebt", len(wjwlijst), "dingskes ingegeven. Deze zijn:")
for Nogiet in wjwlijst:
    print(Nogiet)
