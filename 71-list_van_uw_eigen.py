print("Geeft is dingen da ge in een lijst wilt")
wjwlijst = []
Nogiet = "ja"
while Nogiet.lower() == "ja":
    print("Geeft nog is iet")
    wjwlijst.append(input())
    print("Nog iets ja of nee?")
    Nogiet = input()
print ("Ge hebt", len(wjwlijst), "dingskes ingegeven. Deze zijn:")
for Nogiet in wjwlijst:
    print(Nogiet)

