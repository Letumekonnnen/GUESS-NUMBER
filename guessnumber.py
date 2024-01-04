import random

def get_user_input():
    while True:
        user_input = input("Type a number: ")
        
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please type a number next time.")

def play_guessing_game():
    top_of_range = get_user_input()
    
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        return
    
    random_number = random.randint(0, top_of_range)
    guesses = 0
    
    while True:
        guesses += 1
        user_guess = get_user_input()
        
        if user_guess == random_number:
            print("Congratulations! You guessed the number.")
            break
        elif user_guess > random_number:
            print("Too high!")
        else:
            print("Too low!")
    
    print("You guessed it in", guesses, "guesses.")

play_guessing_game()