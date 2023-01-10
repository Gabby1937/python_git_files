#I want us to work on functions today
#if you can see this signify in the comment section


import random

words = ["Rock", "Papper", "Scissors"]
    


def play():
    print("""
    To play select any letter:
        s for Scissors
        r for Rock
        p for Papper
        """)
    item = input("Select your choice for the game: ")
    pick = random.choice(words)
    if item == 's':
        print("You: Scissors")
        item = 'Scissors'
        if pick == 'Rock':
            print("A.I: Rock")
            print("Rock smashed Scissors!")
            print("You lost!")
        elif pick == 'Scissors':
            print("A.I: Scissors")
            print("It's a draw!")
            print("No winner!")
        elif pick == 'Papper':
            print("A.I: Papper")
            print("Scissors cuts the Papper!")
            print("You win!!!")


        
    elif item == 'r':
        print("You: Rock")
        item = 'Rock'
        if pick == 'Rock':
            print("A.I: Rock")
            print("It's a draw!")
            print("No Winner!")
        elif pick == 'Scissors':
            print("A.I: Scissors")
            print("Rock smashed Scissors!")
            print("You win!!!")
        elif pick == 'Papper':
            print("A.I: Papper")
            print("Papper Wraps Rock!")
            print("You Lost!")

            
    elif item == 'p':
        print("You: Papper")
        item = 'Papper'
        if pick == 'Rock':
            print("A.I: Rock")
            print("Papper Wraps Rock!")
            print("You Win!!!")
        elif pick == 'Scissors':
            print("A.I: Scissors")
            print("Scissors cuts the Papper!")
            print("You Lost!!!")
        elif pick == 'Papper':
            print("A.I: Papper")
            print("It's a draw!!")
            print("No Winner!")
    else:
        print("Wrong input try again!!")
    play()
    
    
play()
