import random

################################################################
number = random.randint(1, 10000000000)
#print("The generated number is {}".format(number))

num_list = [str(random.randint(0, 10)) for n in range(10)]
number = ''.join(num_list)
print(number)
print("The generated ten-digit number is {}".format(number))

def top_up(num):
    num = int(input())
    if num == int(number):
        print("""Your recharge of N{} was successful
        Your account balance is N{}""".format(300, 300+150))
        print('j')


############################################################
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
    
