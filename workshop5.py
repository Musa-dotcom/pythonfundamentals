import random

def guess_random_number(tries, start, stop):
    random_number = random.randint(start, stop)

    # Loop until the user runs out of tries
    while tries > 0:
        #remaining tries
        print("Number of tries left: ", tries)
        user_input = int(input("Guess a number between 0 and 10: "))
        # Check if the user's guess is lower, higher, or equal to the random number
        if user_input < random_number:
            print("Guess higher!")
        elif user_input > random_number:
            print("Guess lower!")
        else:
            print("You guessed the correct number!")
            break
        #decrement the number of tries
        tries -= 1
    
    if tries == 0:
        print("Out of tries. The correct number was:", random_number) 

def guess_random_num_linear(tries, start, stop):
    # Generate a random number within the specified range
    random_number = random.randint(start, stop)

    # Loop until the user runs out of tries
    while tries > 0:
        # Iterate through each number in the range and make a guess
        for guess in range(start, stop + 1):
            print(f"The program is guessing... {guess}")
            print("Number of tries left: ", tries)

        # Check if the program's guess matches the random number
        if guess == random_number:
            print("The program has guessed the correct number!")
            return
        else:
            print("Program failed toguess the correct number")

        print("Out of tries. The correct number was:", random_number)
        #decrement tries
        tries -= 1

import random

def guess_random_num_binary(tries, start, stop):
    #Initialize the lower and upper bounds for binary search
    low = start
    high = stop

    # Generate a random target number within the specified range
    target_number = random.randint(start, stop)

    while tries > 0:
        # Calculate the middle point of the current range
        mid = (low + high) // 2

        # Check if the middle point matches the target number
        if mid == target_number:
            print("Found it!", target_number)
            return
        
        elif mid < target_number:
            low = mid + 1
            print("Guessing higher!")
        else:
            high = mid - 1
            print("Guessing lower!")

        # Decrement tries
        tries -= 1

    print("Out of tries. The correct number was:", target_number)

#Bonus Task

#Function to guess a random number using linear search
def guess_random_num_linear(tries, start, stop):    
    target_number = random.randint(start, stop)
    guesses = set()

    while tries > 0:
        #Getting user input
        guess = int(input("Enter your guess: "))
        #Check if the guess has already been made
        if guess in guesses:
            print("You've already guessed that number. Try again.")
            continue
        
        #Add the guess to the set of guesses
        guesses.add(guess)

        #Check if the guess is correct
        if guess == target_number:
            print("Congratulations! You guessed the correct number.")
            return True
        else:
            print("Incorrect guess. Try again.")
        
        # decrement the number of tries
        tries -= 1

    print("Out of tries. The correct number was:", target_number)
    return False

#Function to guess a random number using binary search
def guess_random_num_binary(tries, start, stop):

    low = start
    high = stop
    
    target_number = random.randint(start, stop)
    # Set to store guesses to prevent duplicate guesses
    guesses = set()

    while tries > 0:
        # Calculate the mid-point for binary search
        mid = (low + high) // 2
        print(f"The program is guessing... {mid}")

        if mid == target_number:
            print("The program has guessed the correct number!")
            return True
        #Update the boundaries based on the guess
        elif mid < target_number:
            low = mid + 1
        else:
            high = mid - 1
        #decrement tries
        tries -= 1

    print("Out of tries. The correct number was:", target_number)
    return False

# Function to let the user choose the guesses and run the game
def guess_random_num():
    # Get user input for number of tries and range
    tries = int(input("Enter the number of tries: "))
    start = int(input("Enter the start of the range: "))
    stop = int(input("Enter the stop of the range: "))

    while True:
        # Prompt user to choose a variation
        choice = input("Choose a variation (user input / linear search / binary search): ").lower()
        if choice == "user input":
            if guess_random_num_linear(tries, start, stop):
                return True
        elif choice == "linear search":
            if guess_random_num_linear(tries, start, stop):
                return True
        elif choice == "binary search":
            if guess_random_num_binary(tries, start, stop):
                return True
        else:
            print("Invalid choice. Please try again.")

# Function to implement the gambling game
def gambling_game():
    balance = 10  # Starting balance

    while balance > 0 and balance <= 50:
        # Prompt player to place a bet
        bet = int(input(f"Your current balance is ${balance}. Place your bet (between $1 and ${min(10, balance)}): "))
        if bet < 1 or bet > min(10, balance):
            print("Invalid bet amount. Try again.")
            continue

        result = guess_random_num_linear(5, 0, 10)

        # Update balance based on the result of the game
        if result:
            balance += bet
            print(f"Congratulations! You've won ${bet}. Your current balance is ${balance}.")
        else:
            balance -= bet
            print(f"Sorry, you've lost ${bet}. Your current balance is ${balance}.")

    # End game conditions
    if balance <= 0:
        print("You've run out of money. Game over.")
    else:
        print("Congratulations! You've won the game.")


""" guess_random_number(5, 0, 10)

guess_random_num_linear(5, 0, 10)

guess_random_num_binary(5, 0, 100) """

gambling_game()