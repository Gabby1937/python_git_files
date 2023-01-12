#generate a random number and see how many trials it takes for a user to input the right number
import random


t_range = input("Type a  number: ")

#we're converting the input from a str to an int
if t_range.isdigit():
    t_range = int(t_range)

    if t_range <= 0:
        print("Please type a number > 0 next time.")
        quit()

else:
    print('Please type a number next time.')
    quit()
#create a variable that will select a number at random btwn 0 and the inputed number(t_range)
random_num = random.randint(0, t_range)

guesses = 0
#if the condition above is true; tell the user to make a guess from the numbers between o and the inputed number
#convert the input from a str to an int

while True:
    guesses += 1
    guess_num = input("Make a guess: ")
    if guess_num.isdigit():
        guess_num = int(guess_num)

    else:
        print('Please type a number next time.')
        continue
    
    if guess_num == random_num:
        print('Correct, You got it right!')
        break

    elif guess_num > random_num:
            print('You were above the number! ')

    else:
        print('You were below the number!')

print('You got it in ', guesses, "guesses")



