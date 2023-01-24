import time

#for  definite loop
#while   indefinite loop
#range(start, stop, [step])
#range(1, 50, 2)
#range is a function used to select two ends in a code


um = 1

while num > 0:
    print("getting number ", num)
    #time.sleep(1)
    num = num + 100
    if num == 1000000000000:
        break
    
    
count = 0

while count < 100:
    time.sleep(1)
    print("get the number ", count)
    count = count + 10
    if count == 50:
        print("Sorry there was a break in transaction was denied")
        break

for things in range(5, 50, 5):
    print(things)
    
    
mart_list = "nose mask", "spagg", "pepper", "meat balls", "tomatoes", "indomie", "onions", "rice", "laptop", "beans", "playstation"

for food in mart_list:
    time.sleep(2)
    print("Buy", food)