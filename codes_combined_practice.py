# Code that counts words in a text.
counts = dict()
line = input("Enter a line of text:")
words = line.split()

print("Words:", words)
print("Counting...")

for word in words:
    counts[word] = counts.get(word, 0) + 1
print("Counts", counts)











def hypotenuse(x, y):
    return ((x**2 + y**2)) ** 0.5

print(hypotenuse(int(input("Enter the length of a shape: ")), int(input("Enter the length of base: "))))


from math import pi
def AoCR(a):
    try:
        a = float(a)
        return (pi*((a/2)**2))
    except ValueError:
        return None
print(AoCR(4))
print(AoCR(5))
print(AoCR(6))

from math import pi
def AoCR(a):
    a = float(a)
    return (pi*((a/2)**2))
print(AoCR(2))
print(AoCR(1))
print(AoCR(3))


def hypotenuse(x, y):
    return ((x**2 + y**2)) ** 0.5

print(hypotenuse(int(input("Enter the length of a shape: ")), int(input("Enter the length of base: "))))





def is_divisible(m, n):
    return m % n == 0

def is_power(m, n):
    if m == 1:
        return True
    if n ==  1:
        return False
    if not is_divisible(m, n):
        return False
    return is_power(m/n, n)                        
    
print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))
quit()


newc = input("Enter new word: ")
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
names.append(newc)
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
        

                            
















friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])

numlist = list()
while True:
    inp = input("Enter a number: ")
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)
    






















papi = input('Give me any number:')
print(papi)
print('This number word came out 3 times')
print(papi*3)
# To convert convert the data from the user i will use the 'int()' function
papi = int(input('Give me any number:'))
print(papi)
print('While this was multiplied by 3')
print(papi*3)


# This quit is to stop our code from going further.
quit()


num = 0
avn = 0.0
while True:
    sval = input("Enter a number: ")
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue
    #print(fval)
    num = num + 1
    avn = avn + fval

#print("All done")
print(avn,num,avn/num)













fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
count = 0
for line in fhand:
    if line.startswith("print"):
        count = count + 1
print("There were", count, "Print lines in", fname)



open
read
write
close

x = input("file name")
file = open(x)

























x = 'driver'
if 'v' in x:
    print('True')

fname = input("Enter your file name")
print(open(fname,r))



list = ['cat', 455, 763.74, 'money', 'Time']

for g in list:
    print(g)



x = 0
while x < 5:
    print("give me a hand")
    print("Please pretty")
    x = x + 1



































fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
count = 0
for line in fhand:
    if line.startswith("print"):
        count = count + 1
print("There were", count, "Print lines in", fname)





fhand = open("SPEEDYBOT.py")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("print"):
        continue
    print(line)





num = 0
tot = 0.0
while True:
    sval = input("Enter a number: ")
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue
    #print(fval)
    num = num + 1
    tot = tot + fval

#print("All done")
print(tot,num,tot/num)







import time
password  = 193752
name = input("Hello what's your name? ")
pin = int(input("Type in your password: "))    


   
#for trials in range(1,6):
   # if pin == password:
       # print("Access Granted!")
        #print("Welcome!", name)
    #else:
       # print("Wrong pin, Try again")
    #break
#print(f"You have exceeded {trials} trials")






def Phone():
    if pin == password:
        print("Access Granted!")
        print("Welcome!", name)
    
    else:
        print("Wrong pin, Try again")

#while trials > 0:
   # trials = trials - 1
for num in range(1, 6):
    if num == 1:
        print("You have exceeded all trials")
    else:
        print(Phone())
        
# Making a phone password lock that waits for 10sec after using up the trials.
# And it will have a limited number of 5 trials.
name = input("Hello what's your name? ")
password  = 193752
def Phone():
    pin = int(input("Type in your password: "))
    if pin == password:
        print("Access Granted!")
        print("Welcome!", name)
    else:
        print("Access Denied")

# Now i have the function above, next call the function repeatedly if wrong.
trials = 6
if num in trials == 5:
    time.sleep(3)
    print(Phone())
else:
    trials -= 1
    print(Phone())

# I need a loop to call the function 5 times
# then if the trials is over wait for 10secs and call the function again.
# New idea, using a counter in loop.

























































