y=0;
a = int(input('enter a='))
b = int(input('enter b='))
c = int(input('enter c='))
k = int(input('enter k='))
if a==0 or b==0 or c==0:
    print ('error')
else :
    y = abs((a**2/b**2 + c**2*a**2)/(a+b+c*(k-a/b**3)) + c + (k/b -k/a)*c)
    print(y)