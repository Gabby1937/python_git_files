d = ('name :', 'address :', 'class :', 'State :')
x = ['John', '46, hover street', 'novice']
g = zip(d, x)

for pair in g:
   print(pair)
print(list(zip(d, x)))

oh = ('chals', 'the', 'hopper')
x = list(oh)
print(x)