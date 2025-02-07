import random

l = ["rock", "scissor", "paper"]

# rock vs scissor -> rock-wins
# rock vs paper -> paper-wins
# paper vs scissor -> scissor-wins

while True:
    ccount = 0
    ucount = 0
    uc = int(input('''
Game Start.....
1. Yes1
2. No | Exit
'''))
    
    if uc == 1:
        for i in range(1, 6):
            userInput = int(input('''
1. Rock
2. Scissor
3. Paper
'''))
            
            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                uchoice = "scissor"
            elif userInput == 3:
                uchoice = "paper"
            else:
                print("Invalid choice. Please choose between 1, 2, or 3.")
                continue  # Skip the rest of the loop iteration if invalid input
            
            Cchoice = random.choice(l)
            
            if Cchoice == uchoice:
                print(f"Computer chose {Cchoice}")
                print(f"You chose {uchoice}")
                print("Game Draw")
            elif (uchoice == "rock" and Cchoice == "scissor") or \
                 (uchoice == "paper" and Cchoice == "rock") or \
                 (uchoice == "scissor" and Cchoice == "paper"):
                print(f"Computer chose {Cchoice}")
                print(f"You chose {uchoice}")
                print("You win!")
                ucount += 1
            else:
                print(f"Computer chose {Cchoice}")
                print(f"You chose {uchoice}")
                print("Computer wins!")
                ccount += 1
        
        print(f"\nFinal scores after 5 rounds: ")
        print(f"You: {ucount} | Computer: {ccount}")
        
    elif uc == 2:
        print("Thanks for playing!")
        break  # Exit the loop and end the game
    else:
        print("Invalid input. Please choose 1 or 2.")


