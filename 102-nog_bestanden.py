import random

bestandsobject = open('ANUSANUS.txt', 'a')
print(random.randint(1,100000000000), file=bestandsobject)
bestandsobject.close()