woord = "in een abjad schrijft ge dees zo ongeveer"
medeklinkers = ''
for letter in woord:
    if letter not in 'aeiou':
        print(letter, end='')
        medeklinkers = medeklinkers + letter
print(medeklinkers)
