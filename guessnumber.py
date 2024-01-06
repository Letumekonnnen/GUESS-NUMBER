import random

def get_user_input():
    while True:
        user_input = input("Type a number: ")
        
        if user_input.isdigit():
            return int(user_input)
        
        print("Please type a valid number.")

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
    
    print(f"You guessed it in {guesses} guesses.")

def play_again():
    while True:
        user_choice = input("Do you want to play again? (yes/no): ")
        
        if user_choice.lower() == "yes":
            play_guessing_game()
        elif user_choice.lower() == "no":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Please enter a valid choice.")

play_guessing_game()
play_again()