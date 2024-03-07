try:
    nummer = int(input('GEEF NE NUMMER: '))
except ValueError:
    exit("DA'S GEEN NUMMER, KNUPPEL")
except KeyboardInterrupt:
    print("\nJA KANKER OP EH")
    exit()
print(nummer / 3)