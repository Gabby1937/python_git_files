# Firstly we import time.
import time

# Next we made four list
gun = ['Metal', 'Bullet', 'String', 'Trigger', 'running']
cloth = ['cotton', 'Tread', 'Needle', 'Pressing Iron', 'Dye']
drum = ['Sticks', 'Fibre', 'Sound Sheet']
hobbies = ['music', 'swimming', 'dancing', 'driving']

# Now we printed out the four list
print('Calling the four list items.')
print(gun)
print(cloth)
print(drum)
print(hobbies)
print('')
print('')
# we made a variable x that added two list together
print("Adding two list items together named 'x' ")
x = gun + cloth

x2 = x[:]
x2.sort()

print(x)
print('')
print('')
print("The variable 'x' has been sorted here")
print(x2)
print('')
print('')
# We printed two items of the x variable.
print('Calling two items from the "x" list using the index numbers.')
print(x[2],x[5])
print('')
print('')
# We added two items to the fourth list using .append
print('Adding two more items to the list called "hobbies".')
hobbies.append(['Reading', 'Jogging'])
print(hobbies)
print('')
print('')
# Now we added all the items of all list to a variable.
all_list = x + drum + hobbies

# Lastly we iterate through the combinded items using the for loop and delaying the
# iteration by a second.
print("Making an iteration through the combinde list.")
for items in all_list:
    time.sleep(1)
    print(items)
