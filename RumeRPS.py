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