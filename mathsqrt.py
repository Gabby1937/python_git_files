# Part 1 code:
def my_sqrt(a):
    while True:
     y = (x + a/x) / 2.0
     if y == x:
        break
     print((x + a/x) / 2.0)
a=4
x=3
y=5
print(my_sqrt(a))


#Part 2 code input:
import math
a=0
math.sqrt(a)
def my_sqrt(a):
    math.sqrt(a)
    return math.sqrt(a)

diff = my_sqrt(a) - math.sqrt(a)
