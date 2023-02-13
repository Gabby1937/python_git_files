import random

words = ["rock", "paper","scissor"]

def grace():
      print("""
            select any of the options:
            R for rock
            P for paper
            S for scissors
            """)
      
      jessica = input("choose an option ")
      cp = random.choice(words)
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
            
        
            
      elif jessica == "p":
            print("you:paper")    
            jessica = "paper"
                      
      else:
            ("wrong input try again")   