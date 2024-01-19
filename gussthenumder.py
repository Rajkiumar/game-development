import random

def guss():
    print("Welcome toGuessing the Number Game!")
    
    lowestnum = 1
    highestnum = 50
    guessnum = random.randint(lowestnum, highestnum)
    
    attempts = 0
    chances = 5
    
    while attempts < chances:
        guess = int(input(f"Guess the number between {lowestnum} and {highestnum}: "))
        
        if guess < guessnum:
            print("Too low! Try again.")
        elif guess > guessnum:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {guessnum} correctly in {attempts + 1} attempts.")
            break
        
        attempts += 1
    
    if attempts == chances:
        print(f"Sorry, you've run out of attempts. The correct number was {guessnum}.")

if __name__ == "__main__":
    guss()
