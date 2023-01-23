# Simultaneous equation.
print('ax + by = c ')
print('dx + ey = f ')
print('Enter the following values :')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = int(input('d = '))
e = int(input('e = '))
f = int(input('f = '))
n = a * e - b * d
print('Values of x and y is :')
if n!=0:
    x = (c*e - b*f)/n
    y = (a*f - c*d)/n
    print('{:.3f} {:3f}'.format(x+0,y+0))