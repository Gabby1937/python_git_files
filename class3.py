import random


def maths(x, y):
    a = [[2, y, 4,],
         [x, 5, 6]]
    print(a[0][1] + a[1][2])
    
def cal():
    x = random.randint(0, 8)
    y = random.randint(0, 8)
    print(x)
    print(y)
    maths(x, y)

quit()
x = 20

while x > 10:
    x -= 1
    print('YES!')
    
