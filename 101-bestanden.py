from time import sleep


knakerneger = open('anusneger.txt', 'r')
print(knakerneger.read())
print(knakerneger)
sleep(5)
for knaker in knakerneger:
    print(knaker)
knakerneger.close

