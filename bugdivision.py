doit = True
number1 = int(input('Enter the number to divide: '))
number2 = int(input('Enter the number to divide by: '))
while doit and number2 == 0:
    print('You cannot divide by zero')
    answer = ''
    while not(answer == 'yes' or answer == 'no'):
        answer = input('Do you want to divide by another number? (yes/no): ')
    if answer == 'yes':
        print("geeft dan is da nummer")
        number2 = int(input())
    else:
        doit = False
if doit == True:
    print(number1, 'divided by', number2, "is", number1 / number2)
else:
    print("stop met de wetten van de fysica te breken, snul")