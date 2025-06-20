import random
import logo_Art7
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5

def set_difficulty(level_chosen):
     if level_chosen=='easy':
         return EASY_LEVEL_ATTEMPTS
     elif level_chosen=='hard':
         return HARD_LEVEL_ATTEMPTS
     else:
         return
     
def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("your guess is two low")
        return attempts-1
    elif guessed_number>answer:
        print("your Guess is too high")
        return attempts-1
    else:
        print(f" your guess is right .. the answer was {answer} ")
        return attempts
      
        
        
def game():    
    print(logo_Art7.logo)    
    print(" let me think of a number between 1 to 50 ")
    answer=random.randint(1,50)
    print(answer)
    level=input("chosse level of difficulty.. type 'easy or 'hard' ").lower()
    attempts=set_difficulty(level)
    if attempts!= EASY_LEVEL_ATTEMPTS  and attempts!=HARD_LEVEL_ATTEMPTS:
        print("you have enterd wrong difficulty level..play again!")
        return 
    guessed_number=0

    while guessed_number!=answer:
        
        print(f"you have {attempts} remaining to guess the number.")
        guessed_number=int(input("Guess a number:"))
        attempts=check_answer(guessed_number,answer,attempts)
        
        if attempts==0:
            print("you are out of guesses.. you Lose!")
            return
        elif guessed_number!= answer:
            print("Guess again")

game()
            
