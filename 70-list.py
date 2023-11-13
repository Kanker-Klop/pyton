animalstr =  'bats and cats and dogs and rats'
animalist = animalstr.split()
print (animalist)
while 'and' in animalist:
    animalist.remove('and')
print (animalist)
animalist.insert(1, 'buidelrattene')
print (animalist)
animalist.pop(3)
print(animalist)
print (animalist)
anus = " and ".join(animalist)
print (anus)
