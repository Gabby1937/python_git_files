import random   # imported random library to help the code 

# Creates options for the game
words = ["rock", "paper","scissor"]

# Creates a function for the game.
def grace():
    # Displays options for the users
      print("""
            select any of the options:
            R for rock
            P for paper
            S for scissors
            """)
      
      # recieves user's choice
      jessica = input("choose an option ")
      # computer randomly picks option
      cp = random.choice(words)
      # computer options for rock
      if jessica.lower() == 'r':
            print("cp picks", cp)
            if cp == 'rock':
                  print("jessica: rock")
                  print('cp: rock')
                  print("it's a draw")
            if cp == "scissors":
                  print("jessica: rock")
                  print('cp: scissors')
                  print("rock smashes scissors")
                  print("you won!!")
            elif cp == "paper": 
                  print("jessica: rock") 
                  print("cp: paper") 
                  print("paper covers rock")
                  print("you lost")
            
    # computer options for scissors
      elif jessica == "s":
            print("you:scissors")    
            jessica = "scissors"
            if cp == "paper":
                  print("cp:paper")
                  print("scissors cuts paper")
                  print("you win")
            if cp == "rock":
                  print("cp:rock")
                  print("rock smashes scissors")
                  print("you lose")      
            if cp == "scissors":
                  print("cp:scissors")
                  print("its a draw")
            
        
    # computer options for paper
      elif jessica == "p":
            print("you:paper")    
            jessica = "paper"
            if cp == "paper":
                  print("cp:paper")
                  print("its a draw")
            if cp == "rock":
                  print("cp:rock")
                  print("paper covers rock")
                  print("you win")      
            if cp == "scissors":
                  print("cp:scissors")
                  print("scissors cuts paper")
                  print("you lose")
    # just incase the user type something wrong.
      else:
            ("wrong input try again")   
            
# Calling the function          
grace()