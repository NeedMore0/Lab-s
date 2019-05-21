import random
y=0
print ('guess number from 1 to 10')
num = int(input('enter number '))
y = random.randint(0, 10)
while num != y:
    print('Wrong number, try again')
    num = int(input('enter number '))
print('Great work! Number is right')