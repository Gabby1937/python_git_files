print("Welcome to my computer quiz")

print("Do you want to play? ")
playing = input('Input either "yes" if you are intrested or "no" if you are not: ').lower()

score = 0

if playing == 'yes' :
    print("Okay! Let's play :)")
else:
    print('Okay have a nice day!')
    quit()



answer = input('What does CPU stand for? ').lower()
if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')



answer = input('What does GPU stand for? ').lower()
if answer == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')



answer = input('What does RAM stand for? ').lower()
if answer == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')




answer = input('What does PSU stand for? ').lower()
if answer == "power supply unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print('You got ' + str(score) + ' questions correct!')
print('You got ' + str((score/4) * 100) + '%')




