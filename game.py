import random

def throw_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    return die1, die2, total

def dice_game():
    high_score = 0

    while True:
        print("Current High Score: ", + high_score)
        print("1) Roll dice")
        print("2) Leave game")

        choice = input("Enter your choice: ")

        if choice == "1":
            die1, die2, total = throw_dice()
           
            print(f"You roll a... {die1}")
            print(f"You roll a... {die2}\n")
            print(f"You have rolled a total of: {total}\n")

            if total > high_score:
                high_score = total
                print("New High Score!\n")

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":

    dice_game()