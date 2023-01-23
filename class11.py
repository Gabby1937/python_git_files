d = ('name :', 'address :', 'class :', 'State :')
x = ['John', '46, hover street', 'novice']
g = zip(d, x)

for pair in g:
   print(pair)
print(list(zip(d, x)))

oh = ('chals', 'the', 'hopper')
x = list(oh)
print(x)

(DEFAULT, 'elisha', 9395),
(DEFAULT, 'Desa', 1002),
(DEFAULT, 'John', 1001),
(DEFAULT, 'Danny', 1003),
(DEFAULT, 'Josh', 4322),
(DEFAULT, 'Donal', 9873),
(DEFAULT, 'Presha', 4395),
(DEFAULT, 'Clinton', 7059),
(DEFAULT, 'Sammy', 6422)



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
    
    
for i in range(1, 100, 2):
    print(i)


import time
x = int(input())

while x > 0:
    x = x - 1
    if x % 2 == 0:
        x = x * 3
    else:
        x = x // 2
    time.sleep(0.5)
    print(x)
print("end")