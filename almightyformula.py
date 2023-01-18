a = int(input('a: $'))
b = int(input('b: $'))
c = int(input('c: $'))
x = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
print (f'answer: {x}')
x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
print (f'answer: {x2}')

