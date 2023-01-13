stuff = dict()
print(stuff.get('candy',-1))

type('bad')

if 567 is 567 :
     print("yes")

zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)

tot = 0
for i in range(0,20):
    print(i)
    tot = tot + 1
print(tot)

n = 5
while n > 0 :
    print(n)
    print('All done')
    break




x = 'banana'
y = max(x)
print(y)

def stuff():
    print('Hello')
    return
    print('World')

stuff()




x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')

x = 6
if x == 6 :
      print('Is 6')
      print('Is Still 6')
      print('Third 6')
    
quit()




fhand = open("SPEEDYBOT.py")
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        count[word] = counts.get(word, 0) + 1





word = 'banana'
#print(word[:])

#print(word[:3])

#print(word[3:])


fruit = ['pineapple', 'water-melon', 'mango', 'apple', 'guava', 'paw-paw', 'straw-berry', 'cherry']

print(fruit[:1])
print(fruit[1:2])
print(fruit[2:3])
print(fruit[3:4])
print(fruit[4:6])
print(fruit[6:])

print (len(fruit))

def calculation(x, y):
    if x>=2 and y<=10:
       print(x+y)
       print(x-y)
       print(x*y)
       print(y//x)
       print(x/y)
    else:
        x<=2 and y>=10
        print('invalid input')
   
def calc(num1, num2):
    print("added result: ", num1 + num2)
    print("subtracted result: ", num1 - num2)
    print ("divided result: ", int(num1 / num2))
    print("multiplied result: ", num1 * num2)
calc(40, 20)

import time
password = 16167

for trials in range(1, 6):
    pin = int(input("Enter Password: "))
    if pin != password:
        print('Access Denied')
    
    else:
        print("Access Granted")
        break
        
if pin == password:
    print('Access Granted')
elif trials == 5:
        print("You have exceeded " + str(trials) + " trials.")
        print("Try again in 5 seconds")
        time.sleep(5)
else:
    print("Access Denied")
    print("You have exceeded " + str(trials) + " trials.")


#def in_both(word1, word2):
   # for letter in word1:
    #    if letter in word2:
           # print(letter)
